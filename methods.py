import dearpygui.dearpygui as dpg
import numpy as np
import pandas as pd
from math import sin
from plot import plot
class METHOD_ABSTRACT():
    def read_data(self, filename) -> pd.DataFrame: 
        data = pd.read_csv(filename)
        return data



# ПЕРВОЕ ОБОБЩЕНИЕ ДЖОНСОНА - СНАЧАЛА ИДУТ ДЕТАЛИ С МИНИМАЛЬНЫЙМ ВРЕМЕНЕМ ОБРАБОТКИ НА ПЕРВОМ СТАНКЕ
class FirstJohnsonGeneralizations(METHOD_ABSTRACT):
    def create_count_window(self, filename): 
        data = super().read_data(filename)
        first_row = data.loc[data.index[0]][1::].sort_values()
        with dpg.window(label=f"Первое обощение Джонсона {filename}"):
            dpg.add_text("ВХОДНОЙ МАССИВ ДЕТАЛЕЙ")
            dpg.add_text(data.to_string())
            dpg.add_text("\nПОРЯДОК ЗАПУСКА ДЕТАЛЕЙ")
            dpg.add_text(first_row.to_string())
            dpg.add_text("\nДИАГРАММА ГАНТА")
            plot(data, first_row)
            #with dpg.plot(tag="plot", label="ДИАГРАММА ГАНТА", height=500, width=600):
            #    dpg.add_plot_legend()
            #    sindatax = []
            #    sindatay = []
            #    for i in range(0, 100):
            #        sindatax.append(i / 100)
            #        if i > 50:
            #            sindatay.append(2)
            #        else:
            #            sindatay.append(1)
            #    # REQUIRED: create x and y axes
            #    dpg.add_plot_axis(dpg.mvXAxis, label="ВРЕМЯ ОБРАБОТКИ")
            #    dpg.add_plot_axis(dpg.mvYAxis, label="СТАНОК", tag="yaxis")
            #    # series belong to a y axis
            #    #dpg.add_area_series(sindatax, sindatay, label="Деталь 1", parent="yaxis", tag="series_data", contribute_to_bounds =True)
            #    dpg.add_bar_series([4,5], [1,1], label="Деталь 1", parent="yaxis", tag="series_data1", horizontal=True)
            #    dpg.add_bar_series([1,1], [3,3], label="Деталь 2", parent="yaxis", tag="series_data2", horizontal=True)
            #    dpg.custom_series([4,5], [1,1], 2, label="Custom Series", tag="demo_custom_series")

# ВТОРОЕ ОБОБЩЕНИЕ ДЖОНСОНА - СНАЧАЛА ИДУТ ДЕТАЛИ С МАКСИМАЛЬНЫМ ВРЕМЕНЕМ ОБРАБОТКИ НА ПОСЛЕДНЕМ СТАНКЕ
class SecondJohnsonGeneralizations(METHOD_ABSTRACT):
    def create_count_window(self, filename): 
        data = super().read_data(filename)
        last_row = data.loc[data.index[-1]][1::].sort_values(ascending=False)
        with dpg.window(label=f"Второе обощение Джонсона {filename}"):
            dpg.add_text("ВХОДНОЙ МАССИВ ДЕТАЛЕЙ")
            dpg.add_text(data.to_string())
            dpg.add_text("\nПОРЯДОК ЗАПУСКА ДЕТАЛЕЙ")
            dpg.add_text(last_row.to_string())
            plot(data, last_row)

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