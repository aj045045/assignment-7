from flask import Flask, render_template,request
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
import numpy as np

app = Flask(__name__)

itemsq1 = ['Average Salary Of Each Position', 'Total number of male and female employee', 'Salary earn by experience example between 10 to 15 year', 'Num of Position in Company','Which position is better in terms of salary'] 
itemsq2 = ['Rating of Products','Top 10 Products by Total','Price Growth Total']

plt.switch_backend('Agg')
@app.route("/")
def index():
    return render_template("welcome.html",itemsq1=itemsq1,itemsq2=itemsq2)

@app.route("/question-1")
def question1():
    plot_urls = []

    empDf = pd.read_csv("./dataset/Employee_data.csv")
    avgSalary = empDf.groupby('Position')['Salary'].mean()
    # Q1
    img = io.BytesIO()
    plt.figure(figsize=(12, 8)) 
    plt.bar(avgSalary.index, avgSalary, color='orange',)
    plt.xlabel('Position', fontsize=20)
    plt.ylabel('Average Salary', fontsize=20)
    plt.xticks(rotation=90, fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()  
    plt.savefig(img,format='png')
    plt.close()
    img.seek(0)
    plot_urls.append(base64.b64encode(img.getvalue()).decode('utf-8'))
    img.truncate(0)
    img.seek(0)
    
    # Q2
    plt.figure(figsize=(12, 8)) 
    male = empDf[empDf['Gender'] == 'M'].count()['Gender']
    female = empDf[empDf['Gender'] == 'F'].count()['Gender']
    plt.pie([male,female],colors=['red','pink'],  labels=['Male', 'Female'],autopct='%1.1f%%',textprops={'fontsize':20})
    plt.tight_layout()  
    plt.savefig(img,format='png')
    plt.close()
    img.seek(0)
    plot_urls.append(base64.b64encode(img.getvalue()).decode('utf-8'))
    img.truncate(0)
    img.seek(0)
    
    # Q3
    plt.figure(figsize=(12, 8)) 
    experienceDf = empDf[(empDf['Experience (Years)'] >= 10) & (empDf['Experience (Years)'] <= 15)][['Position','Salary']]
    plt.bar(experienceDf['Position'],experienceDf['Salary'], color='mediumorchid')
    plt.xlabel('Position',fontsize=15)
    plt.ylabel('Average Salary',fontsize=15)
    plt.xticks(rotation=90)
    plt.tight_layout()  
    plt.savefig(img,format='png')
    plt.close()
    img.seek(0)
    plot_urls.append(base64.b64encode(img.getvalue()).decode('utf-8'))
    img.truncate(0)
    img.seek(0)
    
    # Q4
    noOfPosition = dict()
    for i in empDf['Position'].unique():
        noOfPosition[i] = int(empDf[empDf['Position'] ==i]['Position'].count())
    plt.figure(figsize=(12, 8)) 
    plt.bar(noOfPosition.keys(),noOfPosition.values(),color=['limegreen'])
    plt.xlabel('Position',fontsize=15)
    plt.ylabel('No. Of Position',fontsize=15)
    plt.xticks(rotation=90)
    plt.tight_layout()  
    plt.savefig(img,format='png')
    plt.close()
    img.seek(0)
    plot_urls.append(base64.b64encode(img.getvalue()).decode('utf-8'))
    img.truncate(0)
    img.seek(0)
    
    # Q5
    plt.figure(figsize=(12, 8)) 
    avg_salary = empDf.groupby('Position')['Salary'].mean()
    labels = avg_salary.index
    sizes = avg_salary.values
    plt.figure(figsize=(8, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.axis('equal') 
    plt.tight_layout()  
    plt.savefig(img,format='png')
    plt.close()
    img.seek(0)
    plot_urls.append(base64.b64encode(img.getvalue()).decode('utf-8'))
    img.truncate(0)
    img.seek(0)
    
    return render_template("q1.html",image=plot_urls,label=itemsq1)

@app.route("/question-2")
def question2():
    plot_urls = []
    fkDf = pd.read_excel("./dataset/Flipkart-Laptops.xlsx")
    
    fkDf.replace('NIL', np.nan, inplace=True)
    fkDf.drop_duplicates(inplace=True)
    fkDf.dropna(how='all',axis=1,inplace=True)
    fkDf.dropna(inplace=True)
    # NOTE - Drop Unused columns
    fkDf.drop(['Description','Link'],axis=1,inplace=True)
    # NOTE - Convert String into number
    fkDf['Rating'] = fkDf['Rating'].str.replace(' Ratings','').str.replace(',','').astype(float)
    fkDf['Reviews'] = fkDf['Reviews'].str.replace(' Reviews','').str.replace(',','').astype(float)
    fkDf['Discount price'] = fkDf['Discount price'].astype(float)
    
    img = io.BytesIO()
    # Q1
    rate = dict()
    label = []
    for i in range(5):
        rate[i] = fkDf[(fkDf['Rating'] >= i)&(fkDf['Rating'] <= i+1)].count()['Rating']
        label.append(f'{i+1} Rating {rate[list(rate.keys())[-1]]}')
    total = sum(rate.values())
    percentage = [(i/total)*100 for i in rate.values()]
    print(sum(percentage))
    plt.figure(figsize=(12, 8)) 
    plt.pie(percentage,labels=label,explode=tuple(0.05 for _ in range(len(rate))))
    plt.tight_layout()
    plt.savefig(img,format='png')
    plt.close()
    img.seek(0)
    plot_urls.append(base64.b64encode(img.getvalue()).decode('utf-8'))
    img.truncate(0)
    img.seek(0)
    
    # Q2
    plt.figure(figsize=(12, 8)) 
    fkDf['Total'] = fkDf['Actual price'] - fkDf['Discount price']
    top10DF= fkDf.sort_values(by='Total', ascending=False).head(20)
    plt.bar(top10DF['ProductID'],top10DF['Total'])
    plt.xticks(rotation=90)
    plt.xlabel('Product ID')
    plt.ylabel('Total')
    plt.title('Top 10 Products by Total')
    plt.tight_layout()
    plt.savefig(img,format='png')
    plt.close()
    img.seek(0)
    plot_urls.append(base64.b64encode(img.getvalue()).decode('utf-8'))
    img.truncate(0)
    img.seek(0)
    
    # Q3
    plt.figure(figsize=(12, 8)) 
    plt.plot(fkDf['ProductID'].head(20), fkDf['Total'].head(20), linestyle='--', color='g')
    plt.ylabel("Y-axis Label")
    plt.title("Simple Line Chart")
    plt.xticks([])
    plt.tight_layout()
    plt.savefig(img,format='png')
    plt.close()
    img.seek(0)
    plot_urls.append(base64.b64encode(img.getvalue()).decode('utf-8'))
    img.truncate(0)
    img.seek(0)
    
    return render_template("q1.html",image=plot_urls,label=itemsq2)

@app.route('/graph', methods=['POST'])
def graph():
    title = request.form.get('title')
    src = request.form.get('src')
    return render_template('graph.html', title=title, src=src)


if __name__ == "__main__":
    app.run(debug=True)