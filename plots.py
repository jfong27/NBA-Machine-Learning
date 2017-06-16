import plotly.offline as py
py.init_notebook_mode(connected=True)
from plotly.graph_objs import *
from scipy import stats

import pandas as pd
pd.set_option('display.max_rows', 15)
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


data = pd.read_csv('./nba_data.csv')
champs = data[data.Champion]
others = data[data.Champion == False]

def plot_3pa1():
    
    model = LinearRegression()
    model.fit(data[['3P Attempts']], data['Wins'])
    X = pd.DataFrame({"3P Attempts": np.arange(0, 3500)})
    y_pred = model.predict(X)

    plt.figure(figsize=(12,7))
    plt.plot(X, y_pred, 'r-')
    plt.scatter(x = data[data['3P Attempts'] > 0]['3P Attempts'], y=data[data['3P Attempts'] > 0]['Wins'])
    plt.title('3P Attempts vs Reg. Season Wins')
    
    
def plot_recent_3():
    recent = data[data.Year > 2005]
    model = LinearRegression()
    model.fit(recent[['3P Attempts']], recent['Wins'])
    X = pd.DataFrame({"3P Attempts": np.arange(0, 3500)})
    y_pred = model.predict(X)

    plt.figure(figsize=(12,7))
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


def plot_apg1():
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
    plt.figure(figsize=(12,7))
    three_data = data[data.Year > 1979]
    champ_three = data[(data.Year > 1979) & (data.Champion == True)]
    plt.plot(three_data['Year'], three_data['3P Attempts'], 'c.')
    plt.plot(champ_three['Year'],champ_three['3P Attempts'], 'k.')


def plot_accolades():
    plt.figure(figsize=(12,7))
    plt.plot(champs['Year'], champs['Accolades'], 'y')
    plt.plot(range(1960,2018), others.groupby('Year')['Accolades'].sum()/29)
    plt.title('Accolades on Finals Winner vs League Average')
    plt.legend(['Champion', 'League Average'])
    
    
def plot_apg():
    plt.figure(figsize=(12,7))
    plt.plot(champs['Year'], champs['APG'], 'y')
    plt.plot(range(1960,2018), others.groupby('Year')['APG'].mean())
    plt.title('Assists per Game')
    plt.legend(['Champion', 'League Average'])

    
def plot_rpg():
    plt.figure(figsize=(12,7))
    plt.plot(champs['Year'], champs['RPG'], 'y')
    plt.plot(range(1960,2018), others.groupby('Year')['RPG'].mean())
    plt.title('Rebounds per Game')
    plt.legend(['Champion', 'League Average'])


def plot_tov():
    plt.figure(figsize=(12,7))
    plt.plot(champs[champs.Year > 1974]['Year'], champs[champs.Year > 1974]['TOVPG'], 'y')
    plt.plot(range(1975,2018), others[others.Year > 1974].groupby('Year')['TOVPG'].mean())
    plt.title('Turnovers per Game')
    plt.legend(['Champion', 'League Average'])
    
def plot_fgp():
    plt.figure(figsize=(12,7))
    plt.plot(champs['Year'], champs['FG%'], 'y')
    plt.plot(range(1960,2018), others.groupby('Year')['FG%'].mean())
    plt.title('Field Goal Percentage per Game')
    plt.legend(['Champion', 'League Average'])
    
    
    
def plot_2pa():
    plt.figure(figsize=(12,7))
    plt.plot(champs['Year'], champs['2P Attempts'], 'y')
    plt.plot(range(1960,2018), others.groupby('Year')['2P Attempts'].mean())
    plt.title('2 Point Attempts')
    plt.legend(['Champion', 'League Average'])
    
    
def plot_3pa():

    plt.figure(figsize=(12,7))
    attempts = data.groupby('Year')['3P Attempts'].mean() / data.groupby('Year')['2P Attempts'].mean()
    plt.plot(attempts)
    plt.title('3 Point Attempts')
    plt.legend(['Champion', 'League Average'])
    
    
    
    
def conf_matrix(mat):
    conf_matrix = pd.DataFrame(index = ["Actual True","Actual False"], columns = ["Predict True","Predict False"]).fillna(0)
    if mat == 'dummy': 
        conf_matrix['Predict True']['Actual True'] = 11
        conf_matrix['Predict False']['Actual False'] = 1222
        conf_matrix['Predict True']['Actual False'] = 47
        conf_matrix['Predict False']['Actual True'] = 47
    elif mat == 'model':
        conf_matrix['Predict True']['Actual True'] = 32
        conf_matrix['Predict False']['Actual False'] = 1243
        conf_matrix['Predict True']['Actual False'] = 26
        conf_matrix['Predict False']['Actual True'] = 26
    else:
        conf_matrix['Predict True']['Actual True'] = 29
        conf_matrix['Predict False']['Actual False'] = 1217
        conf_matrix['Predict True']['Actual False'] = 29
        conf_matrix['Predict False']['Actual True'] = 29
    return conf_matrix

    
    
    
    
    
    
    
    
    
    
    
    