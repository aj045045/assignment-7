"""Question 3 :Apply Secant Method to solve the algebraic equation f(x) = x^3 - 4, a = 1, b = 1.5, E = 0.000001"""

import pandas as pd

class SecantSolver:
    
    def __init__(self,a: float,b: float,E: float):
        self.a = a
        self.b = b
        self.E = E
        self.data = {
            "x0":[],
            "f(x0)":[],
            "x1":[],
            "f(x1)":[],
            "x2":[],
            "f(x2)":[],
            "|(fxi-1)-(fxi)|":[],
        }        

    @staticmethod
    def __fMethod(x:float)-> float:
        return x**3 - 4

    @staticmethod
    def __cCalculation(x: float,y: float) -> float:
        return (y*SecantSolver.__fMethod(x) - x*SecantSolver.__fMethod(y)) / (SecantSolver.__fMethod(x) - SecantSolver.__fMethod(y))
    
    def __setOutput(self,x: float,y: float,xi: float):
        self.data["x0"].append(x)
        self.data["f(x0)"].append(self.__fMethod(x))
        self.data["x1"].append(y)
        self.data["f(x1)"].append(self.__fMethod(y))
        self.data["|(fxi-1)-(fxi)|"].append(xi)

    def calculate(self):
        while True:
            self.data["x2"].append(self.__cCalculation(self.a,self.b))
            self.data["f(x2)"].append(self.__fMethod(self.data["x2"][-1]))
            
            if len(self.data["x2"]) >= 2:
                self.__setOutput(self.a,self.b,abs(self.data["x2"][-1]-self.data["x2"][-2]))
                if (abs(self.data["x2"][-1]- self.data["x2"][-2])) < self.E:
                    break
            else:
                self.__setOutput(self.a,self.b,0)
            self.a = self.b
            self.b = self.data["x2"][-1]
        
        return self.data
    
if __name__ == "__main__":
    a = 1
    b = 1.5
    E = 0.000001
    solver = SecantSolver(a,b,E)
    data = solver.calculate()
    pd.options.display.float_format = '{:.5f}'.format
    print(f"The Secant Table where a={a} b={b} e={E:.6f} :\n{pd.DataFrame(data,index=range(1,len(data['x2'])+1))}")