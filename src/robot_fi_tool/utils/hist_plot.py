import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import plotly
import ast

df = pd.read_csv("/home/acefly/robot_fib/data_v4/fault_effect/fault_effect_no_repetation.csv")


pio.renderers.default = 'browser'

# data
df = df.loc[:, 'fault':'fault_effect']
print(df)
# plotly setup
fig=go.Figure()
x_label = []

for i, col in enumerate(df.columns):
    x_label.append(col)

print(x_label)
# data binning and traces
for i, col in enumerate(df.columns):
    a0=np.histogram(df[col], bins=10, density=False)[0].tolist()
    a0=np.repeat(a0,2).tolist()
    a0.insert(0,0)
    a0.pop()
    a1=np.histogram(df[col], bins=10, density=False)[1].tolist()
    a1=np.repeat(a1,2)

    fig.add_traces(go.Scatter3d(x=[i]*len(a0), y=a1, z=a0,
                                mode='lines',
                                name=col
                               )
                  )

plotly.offline.plot(fig, filename='/home/acefly/robot_fib/plots/Scatter3d_hostogram.html')

fig.show()