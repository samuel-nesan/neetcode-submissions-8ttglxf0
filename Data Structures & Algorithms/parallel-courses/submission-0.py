class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        indegree = [0] * (n+1)
        adj = {i:[] for i in range(1, n + 1)}
        for prev, nxt in relations:
            adj[prev].append(nxt)
            indegree[nxt] += 1

        q = deque()
        for n in range(1, n + 1):
            if indegree[n] == 0:
                q.append(n)
        
        step = 0
        finished = 0

        while q:
            step += 1 # new semester 
            next_q = deque() #next sem courses
            
            while q:
                node = q.popleft() 
                finished += 1

                for neighbor in adj[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        next_q.append(neighbor)
            q = next_q
        return step if finished == n else -1