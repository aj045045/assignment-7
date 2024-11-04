"""Question 5 :Find the root of the following using Birge Vieta Method to five decimal places f(x) = x^3 - x^2 - x + 1, x0 = 0.5"""

import pandas as pd

class BirgeVietaSolver:
    
    def __init__(self,coefficient: str,guess:float,max_iteration=10):
        self.coefficient = [float(v) for v in coefficient.split(",")]  
        self.guess = guess
        self.data = []
        self.max_iteration = max_iteration
        
    @staticmethod
    def __bCalculation(data,guess: float):
        val = data["ai"][len(data["bi"])] + (data["bi"][-1] * guess)
        data["bi"].append(val)

    @staticmethod
    def __cCalculation(data,guess: float):
        val = data["bi"][len(data["ci"])] + (data["ci"][-1] * guess)
        data["ci"].append(val)

    def calculate(self):
        k = 0
        while True:
            data  = {
                    "ai":[],
                    "bi":[],
                    "ci":[],
                    "guess":0,
                }
            data["ai"] = self.coefficient.copy()
            data["bi"].append(self.coefficient[0])
            data["ci"].append(self.coefficient[0])
            data["guess"] = self.guess
            
            while True:
                self.__bCalculation(data,self.guess)
                self.__cCalculation(data,self.guess)
                if len(data["ai"]) == len(data["bi"]) == len(data["ci"]):
                    self.guess = self.guess - (data["bi"][-1]/ data["ci"][-2])
                    break
            self.data.append(data)
            
            k+=1
            if data["bi"][-1] == 0.0 or self.max_iteration <= k:
                break
        return self.data
    
if __name__ == "__main__":
    coefficient = "1, -1, -1, 1"
    guess = 0.5
    solver = BirgeVietaSolver(coefficient,guess,)
    dataList = solver.calculate()
    pd.options.display.float_format = '{:.6f}'.format
    print(f"The Birge Vieta Table where coefficient={coefficient} guess={guess} :")
    for i,data in enumerate(dataList):
        print(f"\n\t\t==={i+1}===\n{pd.DataFrame(data,index=range(1,len(data['ai'])+1))}")
    