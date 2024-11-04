"""2. Write a program to find the value of f (2) using Newton’s Divided Difference interpolation formula for the table of values given below"""

import pandas as pd

class NewtonDividedDifference:
    
    def __init__(self,x:list,fx: list,k: list) -> None:
        if len(x) != len(fx):
            raise ValueError("The length of x and fx must be of same size")
        self.x = x
        self.fx = fx
        self.k = k
        self.df = pd.DataFrame({'x':x})
        self.df['f(x)'] = fx

    def calculate(self):
        n = len(self.fx)
        for j in range(n):
            if j == 0:
                self.df[f'{j}_dd'] = self.fx
            else:
                self.df[f'{j}_dd'] = pd.NA
        
        for j in range(1,n):
            for i in range(n-j):
                self.df.at[i,f'{j}_dd'] = (self.df.at[i+1,f'{j-1}_dd'] - self.df.at[i,f'{j-1}_dd'])/ (self.x[i+j] - self.x[i])
            if self.df[f'{j}_dd'].dropna().tolist().count(0) == n-j:
                break
        self.df.drop(columns='0_dd',inplace=True)
        self.df.dropna(how='all',axis=1,inplace=True)

        for kv in self.k:
            total = self.df['f(x)'][0]
            for j in range(1,len(self.df)-2):
                cal = [kv-x[ran] for ran in range(j)]
                multiply = 1
                for ran in cal:
                    multiply*=ran
                total+=(multiply*self.df[f'{j}_dd'][0])
            print(f'The interpolation of {kv} is \t{total}\n')
        return self.df
    
if __name__ == "__main__":
    x = [-1,0,3,6,7]
    fx = [3,-6,39,822,1611]
    k = [2]
    data = NewtonDividedDifference(x,fx,k)
    response = data.calculate()
    print(response)