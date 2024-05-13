import json
import pathlib
import plotly.express as px
import pandas as pd

path = pathlib.Path("resource/eq_data_30_day_m1.json")
text = path.read_text(encoding="utf-8")
load_obj = json.loads(text)

features = load_obj["features"]

mags, titles, lons, lats = [], [], [], []
for feature in features:
    titles.append(feature["properties"]["title"])
    mags.append(feature["properties"]["mag"])
    lons.append(feature["geometry"]["coordinates"][0])
    lats.append(feature["geometry"]["coordinates"][1])

data = pd.DataFrame(data=zip(lons, lats, titles, mags), columns=["经度", "维度", "位置", "震级"])
data.head()
fig = px.scatter(data, x="经度", y="维度", range_x=[-200, 200], range_y=[-90, 90],
                 width=800, height=800, title="全球地震散点图", size="震级", size_max=10, color="震级",hover_name="位置")
fig.write_html("global_earth.html")
fig.show()
