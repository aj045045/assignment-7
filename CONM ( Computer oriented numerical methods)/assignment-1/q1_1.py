"""Question 1 :Apply Bisection method to solve th algebraic equation f(x) = x^4 + 3x^2 + x - 10 = 0, a = 1, b = 2, E = 0.00001"""

import pandas as pd

class BisectionSolver:
    """The Constructor 
    """
    def __init__(self, a: float, b: float, E: float):
        self.a = a
        self.b = b
        self.E = E
        self.data = {
            "a": [],
            "f(a)": [],
            "b": [],
            "f(b)": [],
            "c": [],
            "f(c)": [],
            "|Ck-Ck-1|": []
        }

    """The Function that is used to solve the equation
    
    Returns:
    float: The floating point by solving equation
    """
    @staticmethod
    def __fMethod(x: float) -> float:
        return x**4 + 3*x**2 + x - 10

    """The Function that is used to set the output
    """
    def __setOutput(self, a: float, b: float, ci: float):
        self.data["a"].append(a)
        self.data["f(a)"].append(self.__fMethod(a))
        self.data["b"].append(b)
        self.data["f(b)"].append(self.__fMethod(b))
        self.data["|Ck-Ck-1|"].append(ci)

    """Logic for calculating the Bisection
    """
    def calculate(self):
        self.data["c"].append((self.a + self.b) / 2)
        self.data["f(c)"].append(self.__fMethod(self.data["c"][-1]))
        self.__setOutput(self.a, self.b, 0)

        while True:
            if self.__fMethod(self.a) * self.__fMethod(self.data["c"][-1]) < 0:
                self.b = self.data["c"][-1]
            elif self.__fMethod(self.a) * self.__fMethod(self.data["c"][-1]) > 0:
                self.a = self.data["c"][-1]
            else:
                break

            self.data["c"].append((self.a + self.b) / 2)
            self.data["f(c)"].append(self.__fMethod(self.data["c"][-1]))

            if len(self.data["c"]) >= 2:
                self.__setOutput(self.a, self.b, abs(self.data["c"][-1] - self.data["c"][-2]))
            else:
                self.__setOutput(self.a, self.b, 0)

            if abs(self.data["c"][-1] - self.data["c"][-2]) < self.E:
                break
        return self.data

        
if __name__ == "__main__":
    a = 1
    b = 2
    E = 0.00001
    solver = BisectionSolver(a, b, E)
    data = solver.calculate()
    print(f"The Bisection Table where a={a} b={b} e={E:.5f} :\n{pd.DataFrame(data, index=range(1, len(data['c']) + 1))}")