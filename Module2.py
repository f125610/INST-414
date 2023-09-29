import requests
import json
import pprint

import numpy as np
import pandas as pd
import networkx as nx

URL = "https://mhw-db.com/weapons"
response = requests.get(URL)

api_data = response.json()

g = nx.Graph()
for line in api_data:
    this_weapon = line
    g.add_node(line['id'])
    g.add_node(line['type'])
    g.add_edge(line['id'], line['type'])

print(len(g.nodes()))
print(len(g.edges()))

nx.write_graphml(g, "weapons_type.graphml")

top_k = 10
centrality_degree = nx.degree_centrality(g)

# sort node-centrality dictionary by metric, and reverse to get top elements first
for u in sorted(centrality_degree, key=centrality_degree.get, reverse=True)[:top_k]:
    print(u, centrality_degree[u])

