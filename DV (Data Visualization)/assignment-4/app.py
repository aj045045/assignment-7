import io
import base64
import matplotlib.pyplot as plt
from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import io
import base64
import matplotlib.pyplot as plt
import plotly.io as pio
import matplotlib

matplotlib.use('Agg')

app = Flask(__name__)

class ImagePlot:
    """
    Class for creating and encoding plots using Matplotlib.

    This class provides methods to generate plots and convert them 
    to base64 encoded format for easy storage or transmission.
    """
    @staticmethod
    def plot_image(plot_func):
        """
        Generate a plot and return it as a base64 encoded string.
        
        Parameters:
            plot_func (callable): A function that creates the plot.
        
        Returns:
            str: A base64 encoded string representing the generated plot.
        """
        # Call the function to get the figure
        fig = plot_func()
        
        if isinstance(fig, plt.Figure):
            # Handle Matplotlib figures
            buf = io.BytesIO()
            fig.savefig(buf, format='png')
            plt.close(fig)
            buf.seek(0)
            img_base64 = base64.b64encode(buf.read()).decode('utf-8')
        else:
            # Handle Plotly figures
            img_bytes = pio.to_image(fig, format='png')
            img_base64 = base64.b64encode(img_bytes).decode('utf-8')
        
        return img_base64

itemsq1 = [
    "Pie Chart for How many students got more than 70 score, between 60 to 70, between 40 to 60 and below 40 in math.",
    "Pie Chart for How many students got more than 70 score, between 60 to 70, between 40 to 60 and below 40 in reading.",
    "Pie Chart for How many students got more than 70 score, between 60 to 70, between 40 to 60 and below 40 in writing.",
    "Bar chart for how many student completed test preparation course and how many student not completed test preparation course.",
    "Line chart for math score of 20 to 30 roll nos.",
    "Display the count with proper design that how many students parent having bachelor and master degree.",
    "In dataset, replace data of lunch for free/reduced to premium and display the count of no of students who choose standard lunch and premium lunch."]

df = pd.read_csv('./StudentsPerformance.csv')
    
def plot_q1():
    i = 'math score'
    above_70 = df[df[i] > 70].shape[0]
    between_60_and_70 = df[(df[i] > 60) & (df[i] <= 70)].shape[0]
    between_40_and_60 = df[(df[i] > 40) & (df[i] <= 60)].shape[0]
    below_40 = df[df[i] <= 40].shape[0]

    values = [above_70,between_60_and_70,between_40_and_60,below_40]
    dist = ["Distinction (Above 70)","First class (Between 70 - 60)","Second class (Between 40 - 60)","Fail (Below 40)"]
    # Plotly interactive pie chart
    fig = px.pie(
        values=values, 
        names=dist, 
        title=f'{i} Score Distribution',
        hover_name=dist
    )
    fig.update_traces(hovertemplate='%{label}: %{value} students')
    return fig

def plot_q2():
    i = 'reading score'
    above_70 = df[df[i] > 70].shape[0]
    between_60_and_70 = df[(df[i] > 60) & (df[i] <= 70)].shape[0]
    between_40_and_60 = df[(df[i] > 40) & (df[i] <= 60)].shape[0]
    below_40 = df[df[i] <= 40].shape[0]

    values = [above_70,between_60_and_70,between_40_and_60,below_40]
    dist = ["Distinction (Above 70)","First class (Between 70 - 60)","Second class (Between 40 - 60)","Fail (Below 40)"]
    # Plotly interactive pie chart
    fig = px.pie(
        values=values, 
        names=dist, 
        title=f'{i} Score Distribution',
        hover_name=dist
    )
    fig.update_traces(hovertemplate='%{label}: %{value} students')
    return fig

def plot_q3():
    i = 'writing score'
    above_70 = df[df[i] > 70].shape[0]
    between_60_and_70 = df[(df[i] > 60) & (df[i] <= 70)].shape[0]
    between_40_and_60 = df[(df[i] > 40) & (df[i] <= 60)].shape[0]
    below_40 = df[df[i] <= 40].shape[0]

    values = [above_70,between_60_and_70,between_40_and_60,below_40]
    dist = ["Distinction (Above 70)","First class (Between 70 - 60)","Second class (Between 40 - 60)","Fail (Below 40)"]
    # Plotly interactive pie chart
    fig = px.pie(
        values=values, 
        names=dist, 
        title=f'{i} Score Distribution',
        hover_name=dist
    )
    fig.update_traces(hovertemplate='%{label}: %{value} students')
    return fig

    
def plot_q4():
    completeTest = df[df['test preparation course'] == "completed"]['Roll No'].count()
    pendingTest = df[df['test preparation course'] == "none"]['Roll No'].count()
    plt.bar(['Complete Test Preparation','Pending Test Preparation'],[completeTest,pendingTest],color=['purple','indigo'])
    plt.title("Parent having complete and pending test preparation")
    plt.xlabel("Test")
    plt.ylabel("No. Of Test")
    return plt.gcf()

def plot_q5():
    x = df[(df['Roll No'] > 20) & (df['Roll No'] < 30)]
    plt.plot(x['math score'],x['Roll No'],'o')
    plt.plot(x['math score'],x['Roll No'])
    plt.title("Line Chart for math score of 20 - 30 roll no")
    plt.xlabel("Math Score")
    plt.ylabel("Roll No.")
    return plt.gcf()

def plot_q6():
    bachelor = df[df['parental level of education'] == "bachelor's degree"]['Roll No'].count()
    master   = df[df['parental level of education'] == "master's degree"]['Roll No'].count()
    plt.bar(['Bachelor\'s degree','Master\'s degree'],[bachelor,master],color=['orange','red'])
    plt.title("Parent having bachelor and master")
    plt.xlabel("Degree")
    plt.ylabel("No. Of Degree")
    return plt.gcf()

def plot_q7():
    newDf = df
    newDf['lunch'] = newDf['lunch'].str.replace('free/reduced','premium')
    standard = newDf[newDf['lunch'] == "standard"]['Roll No'].count()
    premium   = newDf[newDf['lunch'] == "premium"]['Roll No'].count()
    plt.bar(['Premium lunch','Standard lunch'],[premium,standard],color=['teal','green'])
    plt.title("Student having premium and standard")
    plt.xlabel("Lunch")
    plt.ylabel("No. Of student")
    return plt.gcf()

@app.route('/')
def index():
    return render_template('welcome.html',itemsq1=itemsq1)

@app.route('/graph/<int:question>')
def graph(question):
    if 1 == question:
        img = ImagePlot.plot_image(plot_q1)
    elif 2 == question:
        img = ImagePlot.plot_image(plot_q2)
    elif 3 == question:
        img = ImagePlot.plot_image(plot_q3)
    elif 4 == question:
        img = ImagePlot.plot_image(plot_q4)
    elif 5 == question:
        img = ImagePlot.plot_image(plot_q5)
    elif 6 == question:
        img = ImagePlot.plot_image(plot_q6)
    elif 7 == question:
        img = ImagePlot.plot_image(plot_q7)
        
    return render_template('graph.html',title=itemsq1[question-1],src=img)

if __name__ == "__main__":
    app.run(debug=True)