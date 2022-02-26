import pandas as pd
import plotly_express as px

df = pd.read_csv("data.csv")
fig = px.scatter(df, x = "cases", y= "date", color= "country", size_max=60)
fig.show()