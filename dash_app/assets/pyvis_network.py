
from pyvis.network import Network
import pandas as pd
import os
import shutil



tag_net = Network(height="750px", width="100%",
                bgcolor="#ffffff", font_color="black")

# set the physics layout of the network

tag_net.force_atlas_2based()
tag_data = pd.read_csv("csv_files_us_new/adj_edge.csv")
tag_data = tag_data.dropna()
node_data = pd.read_csv("csv_files_us_new/node_data.csv")
node_data = node_data.dropna()
sources = tag_data['Source'].astype(str)
targets = tag_data['Target'].astype(str)
weights = tag_data['Weight']

edge_data = zip(sources, targets, weights)

# create the nodes
category_color = True
tag_net.add_nodes(list(node_data["tag"]),color = list(node_data["color"]), value=list(node_data["count"]), label= list(node_data["tag"]),shape=(["circle"] * len(node_data)), title = list(node_data["category_name"]))

#create the edges
for e in edge_data:
    src = e[0]
    dst = e[1]
    w = e[2]
    try:
        tag_net.add_edge(src, dst, value=w, color="grey")
    except AssertionError:
        pass

tag_net.show_buttons(filter_='physics')
tag_net.show("dash_app/assets/tag_network_us.html", notebook=False)

try:
    shutil.move("lib","dash_app/assets/" )
except shutil.Error:
    pass
    