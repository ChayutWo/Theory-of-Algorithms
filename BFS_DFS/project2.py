"""
Math 590
Project 2
Fall 2019

project2.py

Partner 1: Chayut Wongkamthong
Partner 2:
Date: 10/31/2019
"""

# Import math and other p2 files.
import math
from p2tests import *

"""
BFS/DFS function

INPUTS
maze: A Maze object representing the maze.
alg:  A string that is either 'BFS' or 'DFS'.

OUTPUTS
path: The shortest path from maze.start to maze.exit.
"""
def bdfs(maze, alg):
    # If the alg is not BFS or DFS, raise exception.
    if (alg != 'BFS') and (alg != 'DFS'):
        raise Exception('Incorrect alg! Need BFS or DFS!')

    ##### Your implementation goes here. #####
    # If the algorithm is BFS, create a queue
    # Else, it is DFS, create a stack
    elif alg == 'BFS':
        visitList = Queue()
    else:
        visitList = Stack()

    # Change distance of every vertex in the maze to infinity
    # Set visited of every vertex in the maze to False
    # Set prev of every vertex in the maze to None
    for vertex in maze.adjList:
        vertex.visited = False
        vertex.dist = math.inf
        vertex.prev = None
    # For the start vertex, set dist to 0 and mark visited
    # Push the start vertex into the data structure
    maze.start.visited = True
    maze.start.dist = 0
    visitList.push(maze.start)

    # While the visitList is not empty
    while not visitList.isEmpty():
        # pop the next vertex to be considered
        current = visitList.pop()
        # For each of the neighbors, if not visited
        # push it into visitList, add distance, mark as visited
        # and record prev vertex
        for neighbor in current.neigh:
            if not neighbor.visited:
                visitList.push(neighbor)
                neighbor.visited = True
                neighbor.dist = current.dist + 1
                neighbor.prev = current

    # Now we are ready to trace back from exit to start
    path = []
    lastVisit = maze.exit
    # While we still didn't reach the start, add the last visited vertex
    # to the path
    while not lastVisit.isEqual(maze.start):
        path = [lastVisit.rank] + path
        lastVisit = lastVisit.prev
    return [maze.start.rank] + path
    ##### Your implementation goes here. #####

"""
Main function.
"""
if __name__ == "__main__":
    testMazes(False)
