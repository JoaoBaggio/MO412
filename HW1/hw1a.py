from collections import defaultdict
import random

# random.seed(42)
 
graph = defaultdict(set)

def addEdge(graph,u,v):
    graph[u].add(v)
    graph[v].add(u)

def addNode(graph, n):
    graph[n]
 
def generate_edges(graph):
    edges = []
 
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))
    return edges
 
def average_degree(graph):
    totallinks = 0
    for key in graph.keys():
        totallinks += len(graph[key])
    return totallinks/len(graph)

node_number = 10000

for i in range(1, node_number + 1):
    addNode(graph, i)

p = 0.00040

for i in range(1, node_number + 1):
    for j in range(1, node_number + 1):
        if i < j:
            if random.random() < p:
                addEdge(graph, i, j)

print(average_degree(graph))


