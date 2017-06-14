import plotly.offline as py
py.init_notebook_mode(connected=True)
from plotly.graph_objs import *
from scipy import stats
import pandas as pd
pd.set_option('display.max_rows', 15)
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

data = pd.read_csv('./nba.csv')
data.drop('Unnamed: 0', axis=1, inplace=True)

def scatter_plot(): 
    slope, intercept, r_value, p_value, std_err = stats.linregress(data["2P Attempts"], data.Wins)
    line = slope*data["2P Attempts"]+intercept

    traces = [
        Scatter({
                'x' : data['2P Attempts'],
                'y' : data['Wins'],
                'mode' : 'markers',
                'marker' : {'color' : 'lightblue'},
                'name' : 'Data'
            }),
        Scatter({
            'x' : data["2P Attempts"], 
            'y' : line, 
            'mode' : 'lines',
            'marker' : {'color' : 'violet'},
            'name' : 'Fit'
        })
    ]

    layout = Layout({
            'title' : "2 Points Attempt vs. Number of Wins",
            'xaxis' : {'title' : '2 Points Attempt'},
            'yaxis' : {'title' : 'Number of Wins'}
        })

    fig = Figure(data = traces, layout = layout)

    return py.iplot(fig)