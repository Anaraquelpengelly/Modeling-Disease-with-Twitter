import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


row_labels = ['Self', 'Other', 'News', 'Irrelevant', 'Other Relevant']
column_labels = ['7/13/14', '7/20/14', '7/27/14', '8/3/14', '8/10/14', '8/17/14', '8/24/14', '8/31/14', '9/7/14', '9/14/14', '9/21/14', '9/28/12', '10/5/14', '10/12/14', '10/19/14', '10/26/14', '11/2/14', '11/9/14', '11/30/14', '12/7/14', '12/21/14', '1/4/15']

data = pd.read_csv('dynamicLassoCoef3Heatmap.txt', sep='\t')

fig, ax = plt.subplots()
heatmap = ax.pcolor(data, cmap=plt.cm.Blues)

# put the major ticks at the middle of each cell
ax.set_xticks(np.arange(data.shape[1])+0.5, minor=False)
ax.set_yticks(np.arange(data.shape[0])+0.5, minor=False)

# want a more natural, table-like display
ax.invert_yaxis()
ax.xaxis.tick_top()

ax.set_xticklabels(row_labels, minor=False)
ax.set_yticklabels(column_labels, minor=False)
plt.savefig('heatmap3.png')
