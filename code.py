import pandas as pd
import csv
import plotly.express as px
df = pd.read_csv("write file name")
mean = df.groupby(["column name", "column name"], as_index=False)["column name"].mean()
fig = px.scatter(mean, x="column name", y="column name", size="column name", color="column name")
fig.show()
