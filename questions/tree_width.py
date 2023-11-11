"""
Problem: Tree Width Calculation

Description:
The width of a tree is defined as the greatest number of edges in the longest path between any two nodes within the tree. Given an undirected tree consisting of n nodes numbered from 0 to n - 1, and a list of its edges where each edge [ai, bi] represents a two-way connection between nodes ai and bi, compute the width of the tree.

Function Signature:
def tree_width(edges: List[List[int]]) -> int:

Inputs:
  - edges (List[List[int]]): A list where each element is composed of two integers [ai, bi], denoting an undirected edge between nodes ai and bi.

Returns:
  - int: The width of the tree, which is the length of the longest path between any two nodes.

Examples:
1. Input: edges = [[0,1],[0,2]]
  Output: 2
  Explanation: 
  The longest path in the tree runs between nodes 1 and 2, via node 0. This makes the width 2 (edges 1-0 and 0-2).

2. Input: edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]
  Output: 4
  Explanation: 
  The longest path in the tree is from nodes 3 to 5, along the path 3-2-1-4-5. The width is 4, as there are 4 edges along this path.

Notes:
  - The function should identify the longest path between any two nodes in the tree. This can be done using two breadth-first searches (BFS): the first to find the node farthest from a randomly chosen starting point, and the second BFS from this furthest node to determine the longest path.
  - There are no duplicate edges, and the tree is connected, ensuring there is exactly one path between any pair of nodes.

Tags:
  - Graph Theory
  - Tree
  - Breadth-first Search

"""

def tree_width(edges):
  pass