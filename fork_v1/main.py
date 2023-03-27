import uvicorn, os, base64
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from plot import plot
from fastapi.responses import FileResponse

app = FastAPI(
docs_url='/api/docs',
redoc_url='/api/redoc',
openapi_url='/api/openapi.json'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

FILE_BASEPATH = 'files' 
PLOT_BASEPATH = 'plots'

@app.post(f'/upload_csv/')
async def create_upload_file(uploaded_file: UploadFile = File(...)):
    file_location = f"{FILE_BASEPATH}/{uploaded_file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(uploaded_file.file.read())
    return {"info": f"file '{uploaded_file.filename}' saved at '{file_location}'"}

@app.get(f'/list_csv/')
async def list_csv(): return os.listdir(FILE_BASEPATH)

@app.get(f'/show_csv/')
async def show_csv(filename: str):
    df = pd.read_csv(f'{FILE_BASEPATH}/{filename}')
    return df.to_dict()

@app.get(f'/first_gunt_generalization/plot')
async def plot_graphic(filename: str):
    df = pd.read_csv(f'{FILE_BASEPATH}/{filename}')
    row_order = df.loc[df.index[0]][1::].sort_values()
    plot(df, row_order, f'{PLOT_BASEPATH}/{filename}.png')
    return FileResponse(f"{PLOT_BASEPATH}/{filename}.png")

@app.get(f'/first_gunt_generalization/order')
async def count_order(filename: str):
    df = pd.read_csv(f'{FILE_BASEPATH}/{filename}')
    row_order = df.loc[df.index[0]][1::].sort_values()
    return row_order.to_dict()

@app.get(f'/second_gunt_generalization/plot')
async def plot_graphic(filename: str):
    df = pd.read_csv(f'{FILE_BASEPATH}/{filename}')
    row_order = df.loc[df.index[-1]][1::].sort_values(ascending=False)
    plot(df, row_order, f'{PLOT_BASEPATH}/{filename}.png')
    return FileResponse(f"{PLOT_BASEPATH}/{filename}.png")

@app.get(f'/second_gunt_generalization/order')
async def count_order(filename: str):
    df = pd.read_csv(f'{FILE_BASEPATH}/{filename}')
    row_order = df.loc[df.index[-1]][1::].sort_values(ascending=False)
    return row_order.to_dict()

if __name__=="__main__":
    uvicorn.run("main:app",host='0.0.0.0', port=8080, reload=True)