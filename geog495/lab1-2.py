import plotly.graph_objects as go
import pandas as pd
import numpy as np
from itertools import repeat

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

# Color we are using for origin nodes and links
color = ["#F4AC74", "#9DF474", "#96EAE9", "#E696EA", "#E34270"]
# repeating link colors
link_color = []
link_color.extend(repeat(color[0], 10))
link_color.extend(repeat(color[1], 12))
link_color.extend(repeat(color[2], 14))
link_color.extend(repeat(color[3], 10))
link_color.extend(repeat(color[4], 15))

# Visualization
fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 20,
      thickness = 10,
      label = pNn,
      x = allX,
      y = allY,
      hovertemplate = "%{label}",
      color = color
    ),
    link = dict(
      source = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
                3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],  # indices correspond to labels, eg A1, A2, A1, B1, ...
      target = list(range(5, 67)),
      value = dispatches,
      color = link_color
  ))])

fig.update_layout(
    title=dict(text="Seattle Police Department Crime Dispatches by Precinct 2020<br>" +
                    "Source: " "<a href='https://data.seattle.gov/Public-Safety/SPD-Crime-Data-2008-Present/tazs-3rd5'>"
                    "Seattle public data</a><br>" +
                    '<span style="font-size: 10px;">' +
                    "This infographic looks at the travel of police dispatches throughout Seattle,<br>" +
                    "in which the number of dispatches to a neighborhood varies from area to area due to different crime rates",
               font_size=20),
    font_size=10,
    font_color='black',
    paper_bgcolor = 'white'
)

fig.show()

