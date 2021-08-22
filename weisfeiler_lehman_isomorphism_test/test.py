from igraph import *
import cairo

g1 = Graph()
g1.add_vertices(5)
g1.add_edges([(0,1),(0,2),(0,4),(1,3),(2,4),(3,4)])

g2 = Graph()
g2.add_vertices(5)
g2.add_edges([(0,1),(0,2),(0,4),(1,2),(1,3),(3,4)])

def c_from_l(previous_max,neighbors):
  n  = len(neighbors)
  neighbours_index = sorted(range(n), key=lambda k: neighbors[k])
  neighbors.sort()
  add = 1
  c_describe = []
  s = []
  c = [0 for i in range(0,n)]
  c[neighbours_index[0]]=previous_max+add
  s.append(neighbours_index[0])
  for i in range(1,n):
    if(neighbors[i-1] != neighbors[i]):
      add = add + 1
      c_describe.append(s)
      s = []
    s.append(neighbours_index[i])
    if i == n-1 and s!= []:
      c_describe.append(s)

    c[neighbours_index[i]]=previous_max+add
  return c, c_describe  

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

def weisfeiler_lehman_isomorphism_test(g1,g2):
  canonical_g1 =canonical_form(g1).vs['c']
  canonical_g2 =canonical_form(g2).vs['c']
  canonical_g1.sort()
  canonical_g2.sort()
  return  canonical_g1 == canonical_g2

def canonical_form(graph, print_graph = False):
  canonical_graph = graph
  n = len(graph.vs)
  stop = False
  counter = 0
  canonical_graph.vs["c"] = [1 for i in range(0,n)]
  canonical_graph.vs["l"] = [0 for i in range(0,n)]
  c_describe = [[i for i in range(0,n)]]
  while counter <= n and stop==False:
    previous_c_describe = c_describe
    c_max = max(canonical_graph.vs["c"]) 
    r = list()
    for i in range(0,n):
      neighbors = canonical_graph.vs[i].neighbors()
      L=list()
      for neighbor in neighbors:
        L.append(neighbor.attributes()['c'])
      L.sort()
      r.append(L)
    canonical_graph.vs["l"] = r
    canonical_graph.vs['c'], c_describe = c_from_l(c_max,r)
    c_describe.sort()
    previous_c_describe.sort()
    stop = c_describe == previous_c_describe
    counter=counter+1;
    if print_graph:
      plot_graph(canonical_graph,'c')
  return canonical_graph

# plot_graph(g1)
# plot_graph(g2)
# plot_graph(canonical_form(g1),'c')
# plot_graph(canonical_form(g2),'c')
# canonical_form(g1,True)

# print(weisfeiler_lehman_isomorphism_test(g1,g2))

