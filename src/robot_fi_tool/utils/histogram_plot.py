import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objs as go
from matplotlib.cm import ScalarMappable
import plotly.express as px
import plotly
import matplotlib.pyplot as plt

# generate sample data
import numpy as np
import pandas as pd
import seaborn as sns


# Load data from DataFrame
df = pd.read_csv("/home/acefly/robot_fib/data_v4/fault_effect/fault_effect_no_repetation.csv")


x_test_size = 35


df["fault"] = df["fault"].replace(to_replace=1,value="Noise")
df["fault"] = df["fault"].replace(to_replace=2,value="Stuck_at")
df["fault"] = df["fault"].replace(to_replace=3,value="package_drop")
df["fault"] = df["fault"].replace(to_replace=4,value="offset")


df["fault_effect"] = df["fault_effect"].replace(to_replace=1,value="Tool Thrown")
df["fault_effect"] = df["fault_effect"].replace(to_replace=2,value="Human Collision")
df["fault_effect"] = df["fault_effect"].replace(to_replace=3,value="Back Boundary Collision")
df["fault_effect"] = df["fault_effect"].replace(to_replace=4,value="Side Boundary Collision")
df["fault_effect"] = df["fault_effect"].replace(to_replace=5,value="Front Boundary Collision")
df["fault_effect"] = df["fault_effect"].replace(to_replace=6,value="Controller Failure")


df["time_label"] = df["time_label"].replace(to_replace=2,value="Planning")
df["time_label"] = df["time_label"].replace(to_replace=3,value="Execution")

'''
arr = df['fault_effect'].to_numpy()

labels, counts = np.unique(arr, return_counts=True)
plt.bar(labels, counts, align='center')
plt.gca().set_xticks(labels)
plt.ylabel('Number of Fault Effects', fontsize=12, labelpad=20)
plt.xlabel('Fault Effect', fontsize=12, labelpad=20)

plt.show()

'''
'''


# generate some sample data
x = np.random.normal(0, 1, 1000)
y = np.random.normal(0, 1, 1000)


unique_val = ['Human Collision', 'Back Boundary Collision', 'Side Boundary Collision','Tool Thrown', 'Controller Failure']

df_sorted = df.set_index('fault_effect').loc[unique_val]
print(df_sorted)


colors = {'Human Collision': 'Reds', 'Back Boundary Collision': 'Blues', 'Side Boundary Collision': 'Greens','Tool Thrown': 'Oranges', 'Controller Failure': 'Purples'}

colors_list = ['Reds', 'Blues', 'Greens','Oranges', 'Purples']
counts = pd.crosstab(df['fault_effect'], df['fault'])
# create a heatmap using seaborn
ct = counts.reindex(unique_val)
print(ct)

ct_Human = ct.iloc[[0]]
ct_Back = ct.iloc[[1]]
ct_Side = ct.iloc[[2]]
ct_Tool = ct.iloc[[3]]
ct_Controller = ct.iloc[[4]]

print(ct_Human)

#plt_1 = sns.heatmap(ct_Human, annot=True, cmap='Reds', linewidths=1, square=True, cbar=False, linecolor='black')
#plt_2 = sns.heatmap(ct_Back, annot=True, cmap='Blues', linewidths=1, square=True, cbar=False, linecolor='black')
#plt_3 = sns.heatmap(ct_Side, annot=True, cmap='Greens', linewidths=1, square=True, cbar=False, linecolor='black')
#plt_4 = sns.heatmap(ct_Tool, annot=True, cmap='Greys', linewidths=1, square=True, cbar=False, linecolor='black', fmt='g')
plt_5 = sns.heatmap(ct_Controller, annot=True, cmap='Purples', linewidths=1, square=True, cbar=False, linecolor='black')


# set the axis labels

#plt.xlabel("Fault")
#plt.ylabel("Fault Effect")
#plt.yticks(rotation=0)
# show the plot
plt.show()

'''








fig = px.histogram(df, x="fault", color = "time_label",opacity=0.7)
fig.update_xaxes(
        tickangle = 0,
        title_text = "Fault",
        title_font = {"size": 35},
        title_standoff = 25)

fig.update_yaxes(
        tickangle = 0,
        title_text = "count",
        title_font = {"size": 35},
        title_standoff = 25)
fig.update_layout(xaxis_tickfont=dict(size=20), yaxis_tickfont=dict(size=20))

plotly.offline.plot(fig, filename='/home/acefly/robot_fib/plot_v2/fault_and_time_label.html')





fig2 = px.histogram(df, x="fault_effect", color="time_label",opacity=0.7)

fig2.update_xaxes(
        tickangle = 0,
        title_text = "Fault Effect",
        title_font = {"size": 35},
        title_standoff = 25)

fig2.update_yaxes(
        tickangle = 0,
        title_text = "count",
        title_font = {"size": 35},
        title_standoff = 25)

fig2.update_layout(xaxis_tickfont=dict(size=20), yaxis_tickfont=dict(size=20))


plotly.offline.plot(fig2, filename='/home/acefly/robot_fib/plot_v2/fault_effect_and_time_label.html')

fig3 = px.density_heatmap(df, x="fault", y="fault_effect",
                         marginal_x="histogram",
                         marginal_y="histogram")


fig3.update_xaxes(
        tickangle = 0,
        title_font = {"size": 35},
        title_standoff = 25)

fig3.update_yaxes(
        tickangle = 0,
        title_font = {"size": 35},
        title_standoff = 25)

fig3.update_layout(coloraxis = {'colorscale':'viridis'})
fig3.update_layout(xaxis_tickfont=dict(size=20), yaxis_tickfont=dict(size=20))
plotly.offline.plot(fig3, filename='/home/acefly/robot_fib/plot_v2/fault_and_fault_effect.html')





fig4 = px.density_heatmap(df, x="fault", y="fault_effect",
       facet_col="time_label",

       )

fig4.update_layout(coloraxis = {'colorscale':'viridis'})





plotly.offline.plot(fig4, filename='/home/acefly/robot_fib/plot_v2/fault_and_fault_effect_based_on_time_label.html')




fig5 = go.Figure(go.Histogram2d(
        x=df["fault"],
        y=df["fault_effect"],
        texttemplate= "%{z}",
        textfont=dict(size=30),
        colorscale = 'viridis'
    ))


fig5.update_xaxes(
        tickangle = 0,
        title_text = "Fault",
        title_font = {"size": 35},
        title_standoff = 25)

fig5.update_yaxes(
        tickangle = 0,
        title_text = "Fault Effect",
        title_font = {"size": 35},
        title_standoff = 25)
fig5.update_layout(coloraxis = {'colorscale':'Bluered'})
fig5.update_layout(xaxis_tickfont=dict(size=20), yaxis_tickfont=dict(size=20))

plotly.offline.plot(fig5, filename='/home/acefly/robot_fib/plot_v2/fault_and_fault_effect_histogram2d.html')






# use offset group to have 2d histogram on the same figure

xbins = dict(start=-0.5, end=9.5, size=1)


fig6 = go.Figure(go.Histogram2d(
        x=df["joint"],
        y=df["fault_effect"],
        xbins=xbins,
        autobinx=False,
        texttemplate= "%{z}",
        textfont=dict(size=30),
        colorscale = 'viridis'
    ))


fig6.update_xaxes(
        tickangle = 0,
        tickmode = 'linear',
        tick0 = 0,
        dtick = 1,
        title_text = "Joint",
        title_font = {"size": 35},
        title_standoff = 25)

fig6.update_yaxes(
        tickangle = 0,
        title_text = "Fault Effect",
        title_font = {"size": 35},
        title_standoff = 25)
fig6.update_layout(coloraxis = {'colorscale':'Bluered'})
fig6.update_layout(xaxis_tickfont=dict(size=20), yaxis_tickfont=dict(size=20))


plotly.offline.plot(fig6, filename='/home/acefly/robot_fib/plot_v2/joint_and_fault_effect.html')
'''
'''
xbins2 = dict(start=-0.5, end=9.5, size=1)


fig7 = go.Figure(go.Histogram2d(
        x=df["pose"],
        y=df["fault_effect"],
        xbins=xbins2,
        autobinx=False,
        texttemplate= "%{z}",
        textfont=dict(size=30),
        colorscale = 'viridis'
    ))


fig7.update_xaxes(
        tickangle = 0,
        tickmode = 'linear',
        tick0 = 0,
        dtick = 1,
        title_text = "Pose",
        title_font = {"size": 35},
        title_standoff = 25)

fig7.update_yaxes(
        tickangle = 0,
        title_text = "Fault Effect",
        title_font = {"size": 35},
        title_standoff = 25)
fig7.update_layout(coloraxis = {'colorscale':'Bluered'})
fig7.update_layout(xaxis_tickfont=dict(size=20), yaxis_tickfont=dict(size=20))


plotly.offline.plot(fig7, filename='/home/acefly/robot_fib/plot_v2/pose_and _fault_effect.html')

df_noise = df[df['fault'] == 'Noise']

print(df_noise)
'''
'''
xbins2 = dict(start=-6.5, end=6.5, size=1)

fig8 = go.Figure(go.Histogram2d(
        x=df_noise["mean"],
        y=df_noise["fault_effect"],
        xbins=xbins2,
        autobinx=False,
        texttemplate= "%{z}",
        textfont=dict(size=30),
        colorscale = 'viridis'
    ))


fig8.update_xaxes(
        tickangle = 0,
        tickmode = 'linear',
        tick0 = 0,
        title_text = "Mean",
        title_font = {"size": 35},
        title_standoff = 25)

fig8.update_yaxes(
        tickangle = 0,
        title_text = "Fault Effect",
        title_font = {"size": 35},
        title_standoff = 25)
fig8.update_layout(coloraxis = {'colorscale':'Bluered'})
fig8.update_layout(xaxis_tickfont=dict(size=20), yaxis_tickfont=dict(size=20))


plotly.offline.plot(fig8, filename='/home/acefly/robot_fib/plot_v2/noise_and_mean.html')



xbins2 = dict(start=-6.5, end=6.5, size=1)

fig9 = go.Figure(go.Histogram2d(
        x=df_noise["sd"],
        y=df_noise["fault_effect"],
        #xbins=xbins2,
        #autobinx=False,
        texttemplate= "%{z}",
        textfont=dict(size=30),
        colorscale = 'viridis'
    ))


fig9.update_xaxes(
        tickangle = 0,
        #tickmode = 'linear',
        #tick0 = 0,
        title_text = "Standard Deviation",
        title_font = {"size": 35},
        title_standoff = 25)

fig9.update_yaxes(
        tickangle = 0,
        title_text = "Fault Effect",
        title_font = {"size": 35},
        title_standoff = 25)
fig9.update_layout(coloraxis = {'colorscale':'Bluered'})
fig9.update_layout(xaxis_tickfont=dict(size=20), yaxis_tickfont=dict(size=20))


plotly.offline.plot(fig9, filename='/home/acefly/robot_fib/plot_v2/noise_and_sd.html')
'''
'''
df_offset = df[df['fault'] == 'offset']

print(df_offset)

xbins2 = dict(start=0.5, end=3.5, size=1)

fig9 = go.Figure(go.Histogram2d(
        x=df_offset["offset"],
        y=df_offset["fault_effect"],
        xbins=xbins2,
        autobinx=False,
        texttemplate= "%{z}",
        textfont=dict(size=30),
        colorscale = 'viridis'
    ))


fig9.update_xaxes(
        tickangle = 0,
        tickmode = 'linear',
        tick0 = 0,
        title_text = "Offset value",
        title_font = {"size": 35},
        title_standoff = 25)

fig9.update_yaxes(
        tickangle = 0,
        title_text = "Fault Effect",
        title_font = {"size": 35},
        title_standoff = 25)
fig9.update_layout(coloraxis = {'colorscale':'Bluered'})
fig9.update_layout(xaxis_tickfont=dict(size=20), yaxis_tickfont=dict(size=20))


plotly.offline.plot(fig9, filename='/home/acefly/robot_fib/plot_v2/offset_and_fault_effect.html')


'''

'''
xbins2 = dict(start=0.5, end=3.5, size=1)

fig9 = go.Figure(go.Histogram2d(
        x=df["time"],
        y=df["fault_effect"],
        texttemplate= "%{z}",
        textfont=dict(size=30),
        colorscale = 'viridis'
    ))


fig9.update_xaxes(
        tickangle = 0,

        title_text = "Time",
        title_font = {"size": 35},
        title_standoff = 25)

fig9.update_yaxes(
        tickangle = 0,
        title_text = "Fault Effect",
        title_font = {"size": 35},
        title_standoff = 25)
fig9.update_layout(coloraxis = {'colorscale':'Bluered'})
fig9.update_layout(xaxis_tickfont=dict(size=20), yaxis_tickfont=dict(size=20))


plotly.offline.plot(fig9, filename='/home/acefly/robot_fib/plot_v2/time_and_fault_effect.html')
'''
'''
df_pd = df[df['fault'] == 'package_drop']

print(df_pd)

xbins2 = dict(start=0.5, end=3.5, size=1)

fig9 = go.Figure(go.Histogram2d(
        x=df_pd["drop_rate"],
        y=df_pd["fault_effect"],
        xbins=xbins2,
        autobinx=False,
        texttemplate= "%{z}",
        textfont=dict(size=30),
        colorscale = 'viridis'
    ))


fig9.update_xaxes(
        tickangle = 0,
        tickmode = 'linear',
        tick0 = 0,
        title_text = "Offset value",
        title_font = {"size": 35},
        title_standoff = 25)

fig9.update_yaxes(
        tickangle = 0,
        title_text = "Fault Effect",
        title_font = {"size": 35},
        title_standoff = 25)
fig9.update_layout(coloraxis = {'colorscale':'Bluered'})
fig9.update_layout(xaxis_tickfont=dict(size=20), yaxis_tickfont=dict(size=20))


plotly.offline.plot(fig9, filename='/home/acefly/robot_fib/plot_v2/offset_and_fault_effect.html')
