from ..view.plot_graph import *
from igraph import *

class WL:

    """Weisfeiler Lehman Test"""

    def weisfeiler_lehman_isomorphism_test(self, g1, g2):
        canonical_g1 = self.canonical_form(g1).vs['c']
        canonical_g2 = self.canonical_form(g2).vs['c']
        canonical_g1.sort()
        canonical_g2.sort()
        return  canonical_g1 == canonical_g2

    def canonical_form(self, graph, print_graph = False):
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
            canonical_graph.vs['c'], c_describe = self.c_from_l(c_max,r)
            c_describe.sort()
            previous_c_describe.sort()
            stop = c_describe == previous_c_describe
            counter=counter+1;

            if print_graph:
                plot_graph(canonical_graph,'c')
                
        return canonical_graph

    def c_from_l(self, previous_max,neighbors):
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