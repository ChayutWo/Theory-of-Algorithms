"""
Math 590
Project 4
Fall 2019

Partner 1: Chayut Wongkamthong netid: cw403
Partner 2: N/A
Date: 11/30/2019
"""

# Import math, itertools, and time.
import math
import itertools
import time

# Import the Priority Queue.
from p4priorityQueue import *

################################################################################

"""
Prim's Algorithm
Objective: Find minimum spanning tree using Prim's algorithm and change the
           prev attribute of all vertices in the map corresponding to the MST.
Input: adjacency list adjList and adjacency matrix adjMat of the map class
Expected Output: N/A
"""
def prim(adjList, adjMat):
    ##### Your implementation goes here. #####
    # Initialize vertex costs to infinity, prev to None, and visited to False
    for vertex in adjList:
        vertex.cost = math.inf
        vertex.prev = None
        vertex.visited = False

    # Pick one vertex to be the starting tree structure, change the cost to 0
    adjList[0].cost = 0

    # Make priority queue using the costs of vertices
    Q = PriorityQueue(adjList)

    # While the queue is not empty, visit the next closest vertex
    while not Q.isEmpty():
        v = Q.deleteMin()
        v.visited = True
        # For each of its neighbors not visited,
        for neighbor in v.neigh:
            if not neighbor.visited:
                # If new offer is better, update cost and its prev attribute
                if neighbor.cost > adjMat[v.rank][neighbor.rank]:
                    neighbor.cost = adjMat[v.rank][neighbor.rank]
                    neighbor.prev = v
    return

################################################################################

"""
Kruskal's Algorithm
Objective: Find the minimum spanning tree using Kruskal's algorithm
Input: adjacency list adjList and sorted edge list edgeList
Output: List of edges contained in the minimum spanning tree (X)
Note: the edgeList is ALREADY SORTED!
Note: Use the isEqual method of the Vertex class when comparing vertices.
"""
def kruskal(adjList, edgeList):
    ##### Your implementation goes here. #####
    # Initialize all singleton set of each vertex.
    for vertex in adjList:
        makeset(vertex)

    # Initialize empty MST (list of edges in MST)
    X = []

    # Loop through edges in the input edgeList in increasing order
    for e in edgeList:
        # Get the vertices that are connected by that edge
        u, v = e.vertices
        # If the edge connects two different sets, add it to MST
        if find(u) != find(v):
            X.append(e)
            # Then, merge the two sets (union)
            union(u,v)
    return X

################################################################################

"""
Disjoint Set Functions:
    makeset
    find
    union

These functions will operate directly on the input vertex objects.
"""

"""
makeset: this function will create a singleton set with root v.
Input: a vertex object v
"""
def makeset(v):
    ##### Your implementation goes here. #####
    # Set the parent vertex attribute pi to point to itself (v)
    v.pi = v
    # Set the attribute height to 0 (singleton has 0 in height)
    v.height = 0
    return

"""
find: this function will return the root of the set that contains v.
Input: a vertex object v
Expected Output: The parent vertex of v
Note: we will use path compression here.
"""
def find(v):
    ##### Your implementation goes here. #####
    # If we are not at the root (pi is not itself)
    if v != v.pi:
        # Set our parent to be the root of our parent vertex
        v.pi = find(v.pi)

    # Return the root which is our parent
    return v.pi

"""
union: this function will union the sets of vertices v and u.
Input: two vertices u and v of which sets to be union
Expected Output: N/A
"""
def union(u,v):
    ##### Your implementation goes here. #####
    # Find the root of u and v (ru and rv)
    ru = find(u)
    rv = find(v)

    # If they both are in the same set, return
    if ru.rank == rv.rank:
        return

    # If not, make shorter set point to the taller one
    if ru.height > rv.height:
        rv.pi = ru
    elif ru.height < rv.height:
        ru.pi = rv
    else:
        # Same height, break tie, and increase height
        ru.pi = rv
        rv.height += 1
    return

################################################################################

"""
TSP
Objective: Finding an approximate answer to the travelling saleman problem
           using depth first search (DFS)
Input: adjacency list of the map object (adjList) and the start vertex
Expected Output: A list of vertex ranks representing a tour
"""
def tsp(adjList, start):
    ##### Your implementation goes here. #####
    tour = []
    # Mark all vertices in the adjList as unvisited
    for vertex in adjList:
        vertex.visited = False

    # Initialize a stack and push the start into the stack
    s = []
    s.append(start)

    # While the stack is not empty, get the next vertex v to visit
    # Add the rank of the visited vertex into the tour
    while len(s) > 0:
        v = s.pop()
        v.visited = True
        tour.append(v.rank)
        # For each neighbor of v in MST, push it into the stack if not visited
        for neighbor in v.mstN:
            if not neighbor.visited:
                s.append(neighbor)

    # Adding the starting vertex to the tour to make it go back to the start
    tour.append(start.rank)
    return tour

################################################################################

# Import the tests (since we have now defined prim and kruskal).
from p4tests import *

"""
Main function.
"""
if __name__ == "__main__":
    verb = False # Set to true for more printed info.
    print('Testing Prim\n')
    print(testMaps(prim, verb))
    print('\nTesting Kruskal\n')
    print(testMaps(kruskal, verb))
