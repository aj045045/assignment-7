"""Question 2 :Apply False Position Method to solve the algebraic equation f(x) = x^3 - x - 4, a = 1, b = 2, E = 0.00001"""

import pandas as pd

class FalsePositionSolver:
    
    def __init__(self,a:float,b:float,E:float):
        self.a = a
        self.b = b
        self.E = E
        self.data = {
            "a":[],
            "f(a)":[],
            "b":[],
            "f(b)":[],
            "c":[],
            "f(c)":[],
            "|Ck-Ck-1|":[]
        }
    
    @staticmethod
    def __fMethod(x:float) -> float:
        """Calculate the functional value"""
        return x**3 - x - 4
    
    @staticmethod
    def __cCalculation(a:float,b:float) -> float:
        """Calculate the c value for the solution"""
        return (a*FalsePositionSolver.__fMethod(b) - b*FalsePositionSolver.__fMethod(a)) / (FalsePositionSolver.__fMethod(b) - FalsePositionSolver.__fMethod(a))
    
    def __setOutput(self,a:float,b:float,ck:float):
        self.data["a"].append(a)
        self.data["f(a)"].append(self.__fMethod(a))
        self.data["b"].append(b)
        self.data["f(b)"].append(self.__fMethod(b))
        self.data["|Ck-Ck-1|"].append(ck)
        
    def calculate(self):
        self.data["c"].append(self.__cCalculation(self.a,self.b))
        self.data["f(c)"].append(self.__fMethod(self.data["c"][-1]))
        self.__setOutput(self.a,self.b,0)
        
        while True:
            if self.__fMethod(self.a) * self.__fMethod(self.data["c"][-1]) < 0:
                self.b = self.data["c"][-1]
            elif self.__fMethod(self.a) * self.__fMethod(self.data["c"][-1]) > 0:
                self.a = self.data["c"][-1]
            else:
                break
            self.data["c"].append(self.__cCalculation(self.a,self.b))
            self.data["f(c)"].append(self.__fMethod(self.data["c"][-1]))
            
            if len(self.data["c"]) >= 2:
                self.__setOutput(self.a,self.b,abs(self.data["c"][-1] - self.data["c"][-2]))
            else:
                self.__setOutput(self.a,self.b,0)
            
            if self.data["c"][-1] - self.data["c"][-2] < self.E:
                break
        return self.data

if __name__ == "__main__":
    a = 1
    b = 2
    E = 0.00001
    solver = FalsePositionSolver(a,b,E)
    data = solver.calculate()
    
    pd.options.display.float_format = '{:.5f}'.format
    print(f"The False Position Table where a={a} b={b} e={E:.5f} :\n{pd.DataFrame(data, index=range(1, len(data['c']) + 1))}")