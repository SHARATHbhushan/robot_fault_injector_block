import pandas as pd
import plotly
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.lines as mlines

import matplotlib.colors as mcolors
#Read cars data from csv
df = pd.read_csv("/home/acefly/robot_fib/data_v4/fault_effect/fault_effect_no_repetation.csv")

#fig = px.scatter_3d(data, x='joint', y='pose', z='time_label',
#              color='fault_effect',opacity=0.8)

#plotly.offline.plot(fig, filename='/home/acefly/robot_fib/plots/Scatter3d_fault_effect_new.html')


#df = pd.read_csv('data.csv')
counts = df['fault_effect'].value_counts()

# Create a dictionary to map fault_effect values to marker sizes
sizes = {}
for value in counts.index:
    #print(value, counts[value])
    if value == 1:
        sizes[value] = 100
    elif value == 2:
        sizes[value] = 100
    elif value == 3:
        sizes[value] = 100
    elif value == 4:
        sizes[value] = 100
    else:
        sizes[value] = 100




unique_vals = df['fault_effect'].unique()
color_map = plt.get_cmap('tab10')
colors = [color_map(i) for i in np.linspace(0, 1, len(unique_vals))]
color_dict = dict(zip(unique_vals, colors))


# Create a dictionary to map fault_effect values to marker colors

colors = ['darkblue', 'red', 'green', 'cyan', 'magenta']
cmap = mcolors.ListedColormap(colors)
print(cmap)

# planning = 2
df.drop(df[df['time_label'] == 3].index, inplace = True)

print(df['time_label'])


# Create a 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(df['joint'], df['pose'], df['fault'],cmap=cmap, c=df['fault_effect'], marker='o', s=[sizes[val] for val in df['fault_effect']])

# Set axis labels
ax.set_xlabel('Joints',labelpad=10, size=18)

ax.set_ylabel('Poses', labelpad=10, size=18)
ax.set_zlabel('Faults',labelpad=65, size=18)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
ax.set_zticks([1, 2,3,4])
ax.set_zticklabels(['noise', 'stuck at', 'package_drop', 'offset'], size=14)

ax.tick_params(axis='z', pad=30) 

mapping = {1: 'Tool Thrown', 2: 'Human Collision', 3: 'Back Boundary Collision', 4: 'Side Boundary Collision', 6: 'Controller Failure'}

# Replace the values in the 'fault_effect' column using the mapping
unique_val = df['fault_effect'].replace(mapping).unique()


#print(df['fault_effect'])

unique_values = df['fault_effect'].unique()
print(unique_values)
legend_markers = [mlines.Line2D([], [], color=scatter.cmap(scatter.norm([val])), marker='o', linestyle='', markersize=10) for val in unique_values]
ax.legend(legend_markers, unique_val, numpoints=1, loc='upper right', bbox_to_anchor=(1.3, 1))
# Show the plot
plt.show()










'''
#Set marker properties
markercolor = data['fault_effect']

print(markercolor)
#Make Plotly figure
fig1 = go.Scatter3d(x=data['joint'],
                    y=data['pose'],
                    z=data['fault'],
                    marker=dict(color=markercolor,
                                opacity=1,
                                reversescale=True,
                                colorscale='Viridis',
                                size=6),
                    line=dict (width=0.02),
                    mode='markers')

#Make Plot.ly Layout
mylayout = go.Layout(scene=dict(xaxis=dict( title="joint"),
                                yaxis=dict( title="pose"),
                                zaxis=dict(title="fault")),)

#Plot and save html
plotly.offline.plot({"data": [fig1],
                     "layout": mylayout},
                     auto_open=True,
                     filename=("4DPlot.html"))

'''