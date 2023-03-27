import dearpygui.dearpygui as dpg
import numpy as np
import pandas as pd
from math import sin
from plot import plot
import uuid
class METHOD_ABSTRACT():
    def read_data(self, filename:str) -> pd.DataFrame: 
        data = pd.read_csv(filename)
        return data
    



# ПЕРВОЕ ОБОБЩЕНИЕ ДЖОНСОНА - СНАЧАЛА ИДУТ ДЕТАЛИ С МИНИМАЛЬНЫЙМ ВРЕМЕНЕМ ОБРАБОТКИ НА ПЕРВОМ СТАНКЕ
class FirstJohnsonGeneralizations(METHOD_ABSTRACT):
    def create_count_window(self, filename): 
        data = super().read_data(filename)
        first_row = data.loc[data.index[0]][1::].sort_values()
        with dpg.window(label=f"Первое обощение Джонсона {filename}", width= 600, height=800):
            dpg.add_text("ВХОДНОЙ МАССИВ ДЕТАЛЕЙ")
            dpg.add_text(data.to_string())
            dpg.add_text("\nПОРЯДОК ЗАПУСКА ДЕТАЛЕЙ")
            dpg.add_text(first_row.to_string())
            dpg.add_text("\nДИАГРАММА ГАНТА")
            dpg.add_combo(label="Обработанные детали", items = first_row.index.to_list())
            plot(data, first_row)
            width, height, channels, first_image = dpg.load_image("gantt1.png")
            texture_name = str(uuid.uuid4())
            with dpg.texture_registry():
                dpg.add_static_texture(width, height, first_image, tag=texture_name)
            dpg.add_image(texture_name)

                


# ВТОРОЕ ОБОБЩЕНИЕ ДЖОНСОНА - СНАЧАЛА ИДУТ ДЕТАЛИ С МАКСИМАЛЬНЫМ ВРЕМЕНЕМ ОБРАБОТКИ НА ПОСЛЕДНЕМ СТАНКЕ
class SecondJohnsonGeneralizations(METHOD_ABSTRACT):
    def create_count_window(self, filename): 
        data = super().read_data(filename)
        last_row = data.loc[data.index[-1]][1::].sort_values(ascending=False)
        with dpg.window(label=f"Второе обощение Джонсона {filename}", width= 600, height=800):
            dpg.add_text("ВХОДНОЙ МАССИВ ДЕТАЛЕЙ")
            dpg.add_text(data.to_string())
            dpg.add_text("\nПОРЯДОК ЗАПУСКА ДЕТАЛЕЙ")
            dpg.add_text(last_row.to_string())
            dpg.add_combo(label="Обработанные детали", items = last_row.index.to_list())
            plot(data, last_row)
            width, height, channels, first_image = dpg.load_image("gantt1.png")
            texture_name = str(uuid.uuid4())
            with dpg.texture_registry():
                dpg.add_static_texture(width, height, first_image, tag=texture_name)
            dpg.add_image(texture_name)


class ThirdJohnsonGeneralizations(METHOD_ABSTRACT):
    def create_count_window(self, filename): 
        data = super().read_data(filename)

class METH_CONSTR:
    def first_johnson_generalizations(self,) -> FirstJohnsonGeneralizations: 
        return FirstJohnsonGeneralizations()
    def second_johnson_generalizations(self,) -> SecondJohnsonGeneralizations: 
        return SecondJohnsonGeneralizations()
#    def third_johnson_generalizations(self,) -> ThirdJohnsonGeneralizations: 
#        return ThirdJohnsonGeneralizations()