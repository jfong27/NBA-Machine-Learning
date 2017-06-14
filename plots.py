import plotly.offline as py
py.init_notebook_mode(connected=True)
from plotly.graph_objs import *
from scipy import stats

import pandas as pd
pd.set_option('display.max_rows', 15)
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def plot_3pa():
    
    model = LinearRegression()
    model.fit(data[['3P Attempts']], data['Wins'])
    X = pd.DataFrame({"3P Attempts": np.arange(0, 3500)})
    y_pred = model.predict(X)

    plt.plot(X, y_pred, 'r-')
    plt.scatter(x = data[data['3P Attempts'] > 0]['3P Attempts'], y=data[data['3P Attempts'] > 0]['Wins'])
    plt.title('3P Attempts vs Reg. Season Wins')
    
    
def plot_recent_3():
    recent = data[data.Year > 2005]
    model = LinearRegression()
    model.fit(recent[['3P Attempts']], recent['Wins'])
    X = pd.DataFrame({"3P Attempts": np.arange(0, 3500)})
    y_pred = model.predict(X)

    plt.plot(X, y_pred, 'r-')
    plt.scatter(x = recent[recent['3P Attempts'] > 0]['3P Attempts'], y=recent[recent['3P Attempts'] > 0]['Wins'])

    plt.title('3P Attempts vs Reg. Season Wins (Last 12 Years)')
    
def plot_2pa():
    # Copy calculation of split_traces.
    further_split_traces = []
    combinations = ["Golden State Warriors","Cleveland Cavaliers"]
 
    for team in combinations:
        further_split_traces.append(
            Scatter({
                    'x' : np.arange(2010,2018),
                    'y' : data["2P Attempts"][(data.Team == team) & (data.Year >= 2010)],
                    'mode' : 'markers',
                    'name' : team ,
                    'marker' : {'color' : 'red' if team == "Cleveland Cavaliers" else 'yellow',
                                'size' : data["Wins"][(data.Team == team) & (data.Year >= 2010)]},
                    
                })
        )
 
    # Create a layout, as earlier.
    interactive_layout = Layout({
            'title' : "Year vs. 2 Points Attempts",
            'xaxis' : {'title' : 'Year'},
            'yaxis' : {'title' : '2 Points Attempts'},
            'updatemenus' : [{
                    'x' : -0.15,
                    'y' : 1,
                    'yanchor' : 'top',  
                    #'buttons' : buttons
                }]
        })

    interactive_fig = Figure(data = further_split_traces, layout= interactive_layout)
    py.iplot(interactive_fig)


def plot_apg():
    slope, intercept, r_value, p_value, std_err = stats.linregress(data.APG[data.Year >= 2000], data.PPG[data.Year >= 2000])
    line = slope*data.APG[data.Year >= 2000]+intercept

    # Copy calculation of split_traces.
    traces = [
        Scatter({
                'x' : data.APG[data.Year >= 2000],
                'y' : data.PPG[data.Year >= 2000],
                'mode' : 'markers',
                'name' : 'Data'
            }),
        Scatter({
                'x' : data.APG[data.Year >= 2000], 
                'y' : line, 
                'mode' : 'lines',
                'marker' : {'color' : 'orange'},
                'name' : 'Fit'
            })
    ]

    layout = Layout({
            'title' : "APG vs. PPG",
            'xaxis' : {'title' : 'APG'},
            'yaxis' : {'title' : 'PPG'}
        })

    fig = Figure(data = traces, layout = layout)

    py.iplot(fig)



def plot_fga():
    slope, intercept, r_value, p_value, std_err = stats.linregress(data['2P Attempts'][data.Year >= 2000], data.PPG[data.Year >= 2000])
    line = slope*data['2P Attempts'][data.Year >= 2000]+intercept

    # Copy calculation of split_traces.
    traces = [
        Scatter({
                'x' : data['2P Attempts'][data.Year >= 2000],
                'y' : data.PPG[data.Year >= 2000],
                'mode' : 'markers',
                'name' : 'Data'
            }),
        Scatter({
                'x' : data['2P Attempts'][data.Year >= 2000], 
                'y' : line, 
                'mode' : 'lines',
                'marker' : {'color' : 'orange'},
                'name' : 'Fit'
            })
    ]

    layout = Layout({
            'title' : "2PA vs. PPG",
            'xaxis' : {'title' : '2PA'},
            'yaxis' : {'title' : 'PPG'}
        })

    fig = Figure(data = traces, layout = layout)

    py.iplot(fig)
    
    
    
def plot_champs():
    three_data = data[data.Year > 1979]
    champ_three = data[(data.Year > 1979) & (data.Champion == True)]
    plt.plot(three_data['Year'], three_data['3P Attempts'], 'c.')
    plt.plot(champ_three['Year'],champ_three['3P Attempts'], 'k.')



