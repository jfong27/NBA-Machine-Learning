import plotly.offline as py
py.init_notebook_mode(connected=True)
from plotly.graph_objs import *
from scipy import stats

import pandas as pd
pd.set_option('display.max_rows', 15)
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline



def plot_apg():
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


