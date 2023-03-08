import dearpygui.dearpygui as dpg
import numpy as np
import pandas as pd

class METHOD_ABSTRACT():
    def read_data(self, filename) -> pd.DataFrame: 
        data = pd.read_csv(filename)
        return data
    
class FirstJohnsonGeneralizations(METHOD_ABSTRACT):
    def create_count_window(self, filename): 
        data = super().read_data(filename)
        first_row = data.loc[data.index[0]][1::].sort_values()
        with dpg.window(label=f"Первое обощение Джонсона {filename}"):
            dpg.add_text("ВХОДНОЙ МАССИВ ДЕТАЛЕЙ")
            dpg.add_text(data.to_string())
            dpg.add_text("\nПОРЯДОК ЗАПУСКА ДЕТАЛЕЙ")
            dpg.add_text(first_row.to_string())


class SecondJohnsonGeneralizations(METHOD_ABSTRACT):
    def create_count_window(self, filename): 
        data = super().read_data(filename)
        last_row = data.loc[data.index[-1]].sort_values(ascending=False)
        with dpg.window(label=f"Второе обощение Джонсона {filename}"):
            dpg.add_text("ВХОДНОЙ МАССИВ ДЕТАЛЕЙ")
            dpg.add_text(data.to_string())
            dpg.add_text("\nПОРЯДОК ЗАПУСКА ДЕТАЛЕЙ")
            dpg.add_text(last_row.to_string())

class ThirdJohnsonGeneralizations(METHOD_ABSTRACT):
    def create_count_window(self, filename): 
        data = super().read_data(filename)

class METH_CONSTR:
    def first_johnson_generalizations(self,) -> FirstJohnsonGeneralizations: 
        return FirstJohnsonGeneralizations()
    def second_johnson_generalizations(self,) -> SecondJohnsonGeneralizations: 
        return SecondJohnsonGeneralizations()
    def third_johnson_generalizations(self,) -> ThirdJohnsonGeneralizations: 
        return ThirdJohnsonGeneralizations()