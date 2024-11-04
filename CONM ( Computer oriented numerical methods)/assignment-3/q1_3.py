# 1 For the given data below write a program using least square regression to fit a straight line.

import pandas as pd

def least_square_regression(x:list,y:list):
    df = pd.DataFrame({"xi":x,"yi":y})
    n = len(x)
    yi = sum(y)
    xi = sum(x)
    x_bar = xi / n 
    y_bar = yi / n
    df['xi^2'] = [n*n for n in x]
    df['xiyi'] = [df['xi'][i]*df['yi'][i] for i in range(n)]
    df['(yi-y_bar)^2'] = [(df['yi'][i]-y_bar)**2 for i in range(n)]
    a1 = ((n*sum(df['xiyi']))-(xi*yi))/((n*sum(df['xi^2']))-(xi**2))
    a0 = y_bar - (a1*x_bar)
    df['(yi-a0-a1xi)^2'] = [(df['yi'][i] - a0 - (a1*df['xi'][i]))**2 for i in range(n)]
    print(df)
    print("\nThe least square fit y =  ",a1,"+",a0,"x")
if __name__ == "__main__":
    # x = [1,2,3,4,5]
    # y = [0.6,2.4,3.5,4.8,5.7]
    x = [6,7,11,15,17,21,23,29,29,37,39]
    y = [29,21,29,14,21,15,7,7,13,0,3]
    least_square_regression(x,y)