from igraph import *

g = Graph(directed=True)

g.add_vertices(6)

for i in range(len(g.vs)):
    g.vs[i]["id"]= i
    g.vs[i]["label"]= str(i)

g.add_edges([(0,1),(0,2),(1,2),(1,3),(2,1),(2,4),(3,2),(3,5),(4,3),(4,5)])
weights = [16, 13, 10, 12, 4, 14, 9, 20, 7, 4]

g.es['weight'] = weights
g.es['label'] = weights

visual_style = {}
out_name = "graph.png"
visual_style["bbox"] = (400,400)
visual_style["margin"] = 27
visual_style["vertex_color"] = 'white'
visual_style["vertex_size"] = 45
visual_style["edge_curved"] = False
visual_style["autocurve"] = True
my_layout = g.layout_lgl()
visual_style["layout"] = my_layout

# plot(g, out_name, **visual_style)
plot(g, **visual_style)

def BFS(s, t, parent, g):
    ROW = len(g)
    visited = [False]*(ROW)
    queue = []
    queue.append(s)
    visited[s] = True
    while queue:
        u = queue.pop(0)
        for ind, val in enumerate(g[u]):
            if visited[ind] == False and val > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u
                if ind == t:
                    return True
    return False

def ford_fulkerson(source, sink, g):
    ROW = len(g)
    parent = [-1]*(ROW)
    max_flow = 0
    while BFS(source, sink, parent, g):
        path_flow = float("Inf")
        s = sink
        while(s !=  source):
            path_flow = min(path_flow, g[parent[s]][s])
            s = parent[s]
        max_flow +=  path_flow
        v = sink
        while(v !=  source):
            u = parent[v]
            g[u][v] -= path_flow
            g[v][u] += path_flow
            v = parent[v]
    return max_flow

source = 0; sink = 5

print(ford_fulkerson(source, sink, g))