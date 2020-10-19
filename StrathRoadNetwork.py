# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 22:20:44 2020

@author: Clyde007
"""


import networkx as nx
import matplotlib.pyplot as plt
#from classes.bfs import BfsTraverser
import UCSTraverser
G = nx.Graph()
nodes=["SC","Siwaka","Ph.1A","Ph.1B","STC","Phase2","Phase3","J1","Mada","PL"]
G.add_nodes_from(nodes)
G.nodes()#confirm nodes
#Add Edges and their weights
G.add_edge("SC","Siwaka",weight="UnkRoad450m")
G.add_edge("Siwaka","Ph.1A",weight="SangaleRd10m")
G.add_edge("Siwaka","Ph.1B",weight="SangaleLink230m")
G.add_edge("Ph.1A","Ph.1B",weight="ParkingWay100m")
G.add_edge("Mada","Ph.1A",weight="SangaleRd850m")
G.add_edge("Ph.1B","Phase2",weight="KeriRd112m")
G.add_edge("Ph.1B","STC",weight="KeriRd50m")
G.add_edge("STC","Phase2",weight="STCwalkway50m")
G.add_edge("Phase3","Phase2",weight="KeriRd500m")
G.add_edge("Phase2","J1",weight="KeriRd600m")
G.add_edge("J1","Mada",weight="SangaleRd200m")
G.add_edge("STC","PL",weight="LibraryWalkWay250m")
G.add_edge("Phase3","PL",weight="HimaGardensRd350m")
G.add_edge("Mada","PL",weight="LangataRd700m")
#position the nodes to resemble Nairobis map
G.nodes["SC"]['pos']=(0,0)
G.nodes["Siwaka"]['pos']=(2,0)
G.nodes["Ph.1A"]['pos']=(4,0)
G.nodes["Ph.1B"]['pos']=(4,-2)
G.nodes["STC"]['pos']=(4,-4)
G.nodes["Phase2"]['pos']=(6,-2)
G.nodes["J1"]['pos']=(8,-2)
G.nodes["Mada"]['pos']=(10,-2)
G.nodes["Phase3"]['pos']=(8,-4)
G.nodes["PL"]['pos']=(8,-6)
#store all positions in a variable
node_pos = nx.get_node_attributes(G,'pos')
#call BFS to return set of all possible routes to the goal
route_ucs = UCSTraverser()
routes = route_ucs.UCS("SC","PL")
route_list = route_ucs.createVisitedNodes()
#color the nodes in the route_bfs
node_col = ['darkturquoise' if not node in route_list else 'peru' for node in G.nodes()]
peru_colored_edges = list(zip(route_list,route_list[1:]))
#color the edges as well
#print(peru_colored_edges)
edge_col = ['darkturquoise' if not edge in peru_colored_edges else 'peru' for edge in G.edges()]
arc_weight=nx.get_edge_attributes(G,'weight')
nx.draw_networkx(G, node_pos,node_color= node_col, node_size=900)
nx.draw_networkx_edges(G, node_pos,width=4,edge_color= edge_col)
#nx.draw_networkx_edge_labels(G, node_pos,edge_color= edge_col, edge_labels=arc_weight)

nx.draw_networkx_edge_labels(G, node_pos, edge_labels=arc_weight)
plt.axis('off')
plt.show()

