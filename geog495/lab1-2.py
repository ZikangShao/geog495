import plotly.graph_objects as go
import pandas as pd
import numpy as np

crimeData = pd.read_csv('cleaned_2020.csv')
dispatches = crimeData.total_dispatches
# unique precinct values
precinct = crimeData.precinct_station.unique()
# neighborhoods that precincts dispatch to
neighborhood = crimeData.incident_neighborhood
# Combining above two to get labels
pNn = np.concatenate((precinct, neighborhood))

# Node Position values
precinctX = [0.01, 0.45, 0.01, 0.7, 0.45] # precinct x values
precinctY = [0.4, 0.1, 0.9, 0.4, 0.9] # precinct y values
# West precinct neighborhoods x and y values
WNX = np.full((10, ), 0.25)
WNY = np.linspace(0.2, 0.5, num=10)
# North precinct neighborhoods x and y values
NNX = np.full((12, ), 0.65)
NNY = np.linspace(0.01, 0.3, num=12)
# South-west precinct neighborhoods x and y values
SWNX = np.full((14, ), 0.25)
SWNY = np.linspace(0.65, 1, num=14)
# East precinct neighborhoods x and y values
ENX = np.full((10, ), 1)
ENY = np.linspace(0.2, 0.5, num=10)
# South precinct neighborhoods x and y values
SNX = np.full((15, ), 0.75)
SNY = np.linspace(0.65, 1, num=15)
# Combine all the x and y values in two arrays
allX = np.concatenate((precinctX, WNX, NNX, SWNX, ENX, SNX))
allY = np.concatenate((precinctY, WNY, NNY, SWNY, ENY, SNY))

# Visualization
fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 10,
      thickness = 20,
      line = dict(color = "white", width = 0.5),
      label = pNn,
      x = allX,
      y = allY,
      color = ["#FF0000", "#00FFFF", "#800080", "#FFFF00", "#00FF00"]
    ),
    link = dict(
      source = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
                3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],  # indices correspond to labels, eg A1, A2, A1, B1, ...
      target = list(range(5, 67)),
      value = dispatches
  ))])

fig.update_layout(
    title=dict(text="Seattle Police Department Crime Dispatches by Precinct", font_size=30),
    font_size=10,
    font_color='black',
    paper_bgcolor = 'pink'
)
fig.show()

