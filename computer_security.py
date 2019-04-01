import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
from datetime import datetime
from plotly.offline import *


init_notebook_mode(connected=True)

data = pd.read_csv('data.csv')
ip_target = [(1, 'rgb(255,0,0)'), (3, 'rgb(93, 173, 226)'),
             (4, 'rgb(255, 215, 0)'), (5, 'rgb(230, 21, 192)'),
             (6, 'rgb(100, 127, 146)')]

content = []
for ip, color_choice in ip_target:
    temp_data = data.loc[data['l_ipn']==ip]
    temp = go.Scatter(x = temp_data.date,
                        y = temp_data['sumtraffic'],
                        name = 'IP '+ str(ip),
                        line = dict(color = color_choice),
                        opacity = 0.8)
    content.append(temp)

shapes = []
date_target = [datetime(2006, 8, 24), datetime(2006, 9, 4),
               datetime(2006, 9, 18), datetime(2006, 9, 26)]

for i in date_target:
    shapes.append({'type': 'line',
                   'xref': 'x',
                   'yref': 'y',
                   'x0': i,
                   'y0': 0,
                   'x1': i,
                   'y1': 1000000,
                   'line': {'color': 'rgb(211, 211, 211)',
                            'width': 2,
                            'dash': 'dashdot'}})

updatemenus = list([
    dict(active=-1,
         buttons=list([   
            dict(label = 'All',
                 method = 'update',
                 args = [{'visible': [True, True, True, True, True]},
                         {'title': 'Total Traffic of each IP per day'}]),
            dict(label = 'IP 1',
                 method = 'update',
                 args = [{'visible': [True, False, False, False, False]},
                         {'title': 'Total Traffic of IP 1 per day'}]),
            dict(label = 'IP 3',
                 method = 'update',
                 args = [{'visible': [False, True, False, False, False]},
                         {'title': 'Total Traffic of IP 3 per day'}]),
            dict(label = 'IP 4',
                 method = 'update',
                 args = [{'visible': [False, False, True, False, False]},
                         {'title': 'Total Traffic of IP 4 per day'}]),
            dict(label = 'IP 5',
                 method = 'update',
                 args = [{'visible': [False, False, False, True, False]},
                         {'title': 'Total Traffic of IP 5 per day'}]),
            dict(label = 'IP 6',
                 method = 'update',
                 args = [{'visible': [False, False, False, False, True]},
                         {'title': 'Total Traffic of IP 6 per day'}])
        ]),
    )
])

layout = dict(title = 'Total Traffic of each IP per day',
              xaxis = dict(title = 'Date'),
              yaxis = dict(title = 'Total Traffic', type='log',
              	           range = [0, 6]),
              shapes = shapes, updatemenus = updatemenus)

fig = dict(data = content, layout = layout)
plotly.offline.plot(fig, filename = 'TotalTrafficPerIP.html')
