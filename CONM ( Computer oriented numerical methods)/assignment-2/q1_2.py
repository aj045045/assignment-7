"""1. Write a program to find the value of f (0.4) using Lagrange’s interpolation formula for the table of values given below."""

class LagrangeInterPolation:
    
    def __init__(self,x:list,fx:list,k:int) -> None:
        if len(x) != len(fx):
            raise ValueError("The length of x and fx is not same")
        self.x = x
        self.fx = fx
        self.k = k
        
    def calculate(self):
        val = []
        n = len(x)
        for i in range(n):
            numerator = 1
            denominator = 1
            for j in range(n):
                if j != i:
                    numerator*=self.k-self.x[j]
                    denominator*=self.x[i]-self.x[j]
            val.append((numerator*self.fx[i])/denominator)
        print(f"\nThe interpolation of {self.k} is: {sum(val)}")
        
if __name__ == "__main__":
    x = [0.3,0.5,0.6]
    fx = [0.61,0.69,0.72]
    k = 0.4
    data = LagrangeInterPolation(x,fx,k)
    data.calculate()
    