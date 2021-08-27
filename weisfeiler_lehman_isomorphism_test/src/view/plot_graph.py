from igraph import *

def plot_graph(g, key= None):
  value = range(0,len(g.vs))
  if key :
    value = g.vs[key]
  color_dict = {0:'#B6D7A8',1:'#F9CB9C',2:'#FFE599',3:'#A4C2F4',4:'#A2C4C9'}
  g.vs["color"] = [(color_dict[index%5]) for index in range(0,len(g.vs))]
  g.vs["label"] =  value
  g.vs["size"] = 35
  layout = g.layout_kamada_kawai()
  plot(g,layout = layout)