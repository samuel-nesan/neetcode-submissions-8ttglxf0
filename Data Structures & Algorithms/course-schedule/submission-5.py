class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adj[crs].append(pre)
            indegree[pre] += 1
        
        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)
        
        finish = 0
        while q:
            node = q.popleft()
            finish += 1
            for neighbors in adj[node]:
                indegree[neighbors] -= 1
                if indegree[neighbors] == 0:
                    q.append(neighbors)
        return finish == numCourses