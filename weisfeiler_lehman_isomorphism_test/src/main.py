from igraph import *
from .model.WL import WL
from .view.plot_graph import plot_graph

def main():
  g1 = Graph()
  g1.add_vertices(5)
  g1.add_edges([(0,1),(0,2),(0,4),(1,3),(2,4),(3,4)])

  g2 = Graph()
  g2.add_vertices(5)
  g2.add_edges([(0,1),(0,2),(0,4),(1,2),(1,3),(3,4)])

  # plot_graph(g1)
  # plot_graph(g2)

  wl = WL()

  plot_graph(wl.canonical_form(g1),'c')
  plot_graph(wl.canonical_form(g2),'c')

  if(wl.weisfeiler_lehman_isomorphism_test(g1,g2)):
    print('The graphs passed the test of Weisfeiler Lehman')