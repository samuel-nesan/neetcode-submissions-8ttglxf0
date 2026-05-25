class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = {i:[] for i in range(numCourses)}
        for dst, src in prerequisites:
            adj[src].append(dst)
            indegree[dst] += 1
        
        q = deque()

        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)
        
        crsList = []
        while q:
            node = q.popleft()
            crsList.append(node)
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        
        if len(crsList) == numCourses: return crsList
        else: return []