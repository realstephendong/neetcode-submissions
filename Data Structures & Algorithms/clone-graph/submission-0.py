"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        clones = {}
        visited = set()

        def dfs(currnode):
            if currnode in clones:
                return clones[currnode]

            clone = Node(currnode.val)

            clones[currnode] = clone

            for neighbor in currnode.neighbors:
                clone.neighbors.append(dfs(neighbor))
            
            return clone
        

        return dfs(node)