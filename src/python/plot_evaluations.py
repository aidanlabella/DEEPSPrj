import pandas as pd
import plotly.express as px
import sys

df = pd.read_csv(sys.argv[1])

cols = ['predicted_SO4', 'predicted_SO2', 'predicted_O3', 'predicted_CO']

fig = px.line(df, x=df.index, y=cols, title='Predicted vs. Actual')
fig.update_layout(xaxis_title='Timestep', yaxis_title='Values')
fig.show()
