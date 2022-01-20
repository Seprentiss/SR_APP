import pandas as pd
import json
import matplotlib.pyplot as plt

import sys

# Used to read in a Json file

"""
#f = open(sys.argv[1])
# 
# json_input = json.load(f)
# 
# f.close()
"""

# example Json object input with the desired format

json_input = '{"BRO":{"BSN":{"W":10,"L":12},"CHC": {"W":15, "L":7 }},"BSN":{"BRO":{"W":12,"L":10},"CHC": {"W":13, "L":9 }},' \
             '"CHC":{"BRO":{"W":7,"L":15},"BSN": {"W":9, "L":13 }}}'

# Convert the Json object into a dictionary

d = dict(json.loads(json_input))

# Convert the dictionary into a pandas data frame
data = pd.DataFrame(d)

# Replace the NA values caused by teams not playing themselves with dashes
data = data.fillna("--")
for i in data.columns:
    for j in range(len(data)):
        if data[i][j] == "--":
            continue
        else:
            # Place only the Wins # in the cell instead of both the Wins & Losses
            data[i][j] = list(data[i][j].values())[0]

# Add index column title
data.index.name = 'TM'

# Sort the data frame alphabetically
rslt_df = data.sort_index()


# Create matplotlib table plot

#define figure and axes
fig, ax = plt.subplots()

#hide the axes
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')

#create data
df = rslt_df

#create table
table = ax.table(cellText=df.values, colLabels=df.columns, rowLabels = df.index, loc='center',
                 cellLoc='center')

w, h = table[0,1].get_width(), table[0,1].get_height()
table.add_cell(0, -1, w,h, text=df.index.name)

#display table
fig.tight_layout()
plt.show()