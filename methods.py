import dearpygui.dearpygui as dpg
import numpy as np

class METH_CONSTR:
    def method_gauses(self,): 
        return GausMethod()
    def method_second(self,): 
        return SecondMethod()


class METHOD_ABSTRACT():
    def create_count_window(self, filename): 
        DATA = np.loadtxt(filename)
        with dpg.window(label=f"{filename}"):
            dpg.add_text(f"{DATA}")


class GausMethod(METHOD_ABSTRACT):
    def create_count_window(self, filename): 
        super().create_count_window(filename)

class SecondMethod(METHOD_ABSTRACT):
    def create_count_window(self, filename): 
        super().create_count_window(filename)