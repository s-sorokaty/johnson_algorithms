import dearpygui.dearpygui as dpg
from methods import METH_CONSTR

dpg.create_context()

with dpg.font_registry():
    with dpg.font("NotoMono-Regular.ttf", 14) as font1:
        dpg.font_registry()
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)
        dpg.bind_font(font1)


METHODS_LIST = [func for func in dir(METH_CONSTR()) if callable(getattr(METH_CONSTR(), func)) and func[0:2] != '__']
CSV_FILENAME = 'test.csv'
SELECTED_METHOD = ''

def set_csv_filename(id, value): 
    global CSV_FILENAME 
    CSV_FILENAME = value

def set_current_method(id, value):
    global SELECTED_METHOD 
    SELECTED_METHOD = getattr(METH_CONSTR(), value)()

def count(): SELECTED_METHOD.create_count_window(CSV_FILENAME)

dpg.create_viewport(title='Application', width=1000, height=1000)

with dpg.window(label="READER", width=300, height=200):
    dpg.add_input_text(label="CSV файл", default_value=CSV_FILENAME, callback=set_csv_filename)
    dpg.add_combo(label="Метод", items =METHODS_LIST, callback=set_current_method)
    dpg.add_button(label="Расчитать", callback=count)


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()