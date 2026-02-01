"""
1. BUILD adjacency list both directions using equations. for the list, append both the neighbor, and the weight from values
2. run a bfs 
3. bfs -> q + visited hashset . q-> add a tuple of querries, start node , val (holding the total distance) [start, totalVal]
4. add the start to visited as well. pop the node and weight. if the node is target, return the weight. If not, access the node and weight
from adjaceny list. append node + weight*val [basically running count to q]. then add the node to the hashset. return -1. if its not found for that node
5. list compression. call bfs for each pair in querries, then add it to array. 
"""

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for i,eq in enumerate(equations):
            a, b = eq
            adj[a].append([b, values[i]])
            adj[b].append([a, 1/values[i]])
        
        def bfs(start, target):
            if start not in adj or target not in adj:
                return -1
            visited = set()
            queue = deque()
            queue.append([start, 1])
            visited.add(start)
            while queue:
                node, w = queue.popleft()
                if node == target:
                    return w
                for neigh, weight in adj[node]:
                    if neigh not in visited:
                        queue.append([neigh, w*weight])
                        visited.add(neigh)
            return -1
        return [bfs(a[0], a[1]) for a in queries]