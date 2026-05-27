class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        indegree = [0] * (n + 1)
        adj = {i:[] for i in range(n+1)}
        for prev, nxt in relations:
            adj[prev].append(nxt)
            indegree[nxt] += 1
        
        q = deque()
        for i in range(1, n + 1):
            if indegree[i] == 0:
                q.append(i)
        
        semesters = 0

        while q:
            next_q = deque()
            semesters += 1
            while q:
                node = q.popleft()
                
                for neighbors in adj[node]:
                    indegree[neighbors] -= 1
                    if indegree[neighbors] == 0:
                        next_q.append(neighbors)
            q = next_q
        return semesters if max(indegree) == 0 else -1
