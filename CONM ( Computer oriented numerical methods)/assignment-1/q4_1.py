"""Question 4 :Find an approximation to root 12 to five decimal places using Newton Raphson Method x0 = 3.5"""

import pandas as pd

class NewtonRaphsonSolver:

    def __init__(self,a: float,E: float):
        self.a = a
        self.E = E
        self.data = {
            "xi":[],
            "f(xi)":[],
            "f'(xi)":[],
            "xi+1":[],
            "|Ck-Ck-1|":[]
        }
        
    @staticmethod
    def __fMethod(x:float) -> float:
        return x**2 - 12
        # return x ** 3 + x -1 
    
    @staticmethod
    def __fNotMethod(x: float) -> float:
        return 2*x

    def __setOutput(self):
        fx = self.__fMethod(self.a)
        fnx = self.__fNotMethod(self.a)
        xi = self.a - (fx/fnx)
        self.data["xi"].append(self.a)
        self.data["f(xi)"].append(fx)
        self.data["f'(xi)"].append(fnx)
        self.data["xi+1"].append(xi)
        if len(self.data["xi+1"]) >= 2:
            self.data["|Ck-Ck-1|"].append(abs(self.data['xi+1'][-2] - self.data['xi+1'][-1]))
        else:
            self.data['|Ck-Ck-1|'].append(0)
    
    def calculate(self):
        while True:
            self.__setOutput()
            if self.data["|Ck-Ck-1|"][-1] < self.E and len(self.data['|Ck-Ck-1|']) >= 2:
                break
            self.a = self.data["xi+1"][-1]        
        return self.data
    
if __name__ == "__main__":
    a = 3.5
    E = 0.0001
    solver = NewtonRaphsonSolver(a,E)
    data = solver.calculate()
    pd.options.display.float_format = '{:.5f}'.format
    print(f"The Newton Raphson Table where a={a} E={E:.5} :\n{pd.DataFrame(data,index=range(1,len(data['|Ck-Ck-1|'])+1))}")