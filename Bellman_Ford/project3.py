"""
Math 590
Project 3
Fall 2019

Partner 1: Chayut Wongkamthong
Partner 2: N/A
Date: 11/04/2019
"""

# Import math and p3tests.
import math
from p3tests import *

################################################################################

"""
detectArbitrage
Objective: Perform Bellman-Ford Algorithm to detect Arbitrage
Input: currencies - the Currencies object for the exchange rate
       tol - update tolerance
Expected output: A list containing ranks of vertices forming cycle that results
                 in Arbitrage
                 If Arbitrage doesn't exist, return empty list
"""
def detectArbitrage(currencies, tol=1e-15):
    ##### Your implementation goes here. #####

    # Set initial dist and prev
    for vertex in currencies.adjList:
        vertex.dist = math.inf
        vertex.prev = None
    # Assume that we start at the first vertex
    currencies.adjList[0].dist = 0

    # Part I: Perform Bellman-Ford |V|-1 iterations.
    for i in range(len(currencies.adjList)-1):
        # for each vertex in the currencies graph, make offers to neighbors
        for vertex in currencies.adjList:
            for neighbor in vertex.neigh:
                # If the offer is better than the prediction, update parameters.
                distance = currencies.adjMat[vertex.rank][neighbor.rank]
                if neighbor.dist > vertex.dist + distance + tol:
                    neighbor.dist = vertex.dist + distance
                    neighbor.prev = vertex

    # Part II: Perform Bellman-Ford 1 iteration to find changes.
    # Initialize change and changeVertex to keep track of the change in dist
    change = False
    changeVertex = None
    # for each vertex in the currencies graph, make offers to neighbors
    for vertex in currencies.adjList:
        for neighbor in vertex.neigh:
            # If the offer is better than the prediction, update parameters.
            distance = currencies.adjMat[vertex.rank][neighbor.rank]
            if neighbor.dist > vertex.dist + distance + tol:
                neighbor.dist = vertex.dist + distance
                neighbor.prev = vertex
                # Record change and the vertex that is updated
                change = True
                changeVertex = neighbor

    cycle = [] # Initialize the cycle list for output
    # If there are changes in the last loop, there is arbitrage
    if change:
        # Part III: Backtrack the path of the changed vertex until find cycle
        while changeVertex.rank not in cycle:
            cycle = [changeVertex.rank] + cycle
            changeVertex = changeVertex.prev

        # Part IV: Extract only part of the list that is cycle
        # Find position where rank is the same as the start of the loop
        foundLoopEnd = False
        index = 0
        while not foundLoopEnd:
            # If, at that index, the vertex is the end of loop, stop.
            # Else, continue searching.
            if cycle[index]== changeVertex.rank:
                foundLoopEnd = True
            else:
                index += 1
        # Put our starting point into the cycle list and extract the list
        # for parts that contain true cycle (upto index position)
        cycle = [changeVertex.rank] + cycle[:index+1]
    return cycle
    ##### Your implementation goes here. #####

################################################################################

"""
rates2mat
Objective: Create an adjacency matrix to be used in detecting arbitrage
Input: rates - 2d-array representing exchange rates
Expected Output: an adjacency matrix of exchange rates 
"""
def rates2mat(rates):
    ##### Your implementation goes here. #####
    # For each rate in rates, store -log(rate) in the adjacency matrix
    return [[-math.log(R) for R in row] for row in rates]
    ##### Your implementation goes here. #####

"""
Main function.
"""
if __name__ == "__main__":
    testRates()
