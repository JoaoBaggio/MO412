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

for i in range(1, node_number + 1):
    for j in range(1, node_number + 1):
        if i < j:
            e = 0.00001
            q = 4/3
            p = (len(graph[i]) + e)
            s = 0
            for m in range(1, j):
                s += len(graph[m]) + e
            p = p*q/s
            if random.random() < p:
                addEdge(graph, i, j)


print(average_degree(graph))