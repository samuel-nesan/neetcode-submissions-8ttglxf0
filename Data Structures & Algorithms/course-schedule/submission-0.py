class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}
        for i in range(numCourses):
            adjList[i] = []
        for src, dst in prerequisites:
            adjList[src].append(dst)

        topSort = []
        visit = set()
        path = set()
        
        for i in range(numCourses):
            if not self.dfs(i, adjList, visit, path, topSort):
                return False
        return True

    def dfs(self, src, adjList, visit, path, topSort):
        if src in path:
            return False
        if src in visit:
            return True
        visit.add(src)
        path.add(src)

        for neighbor in adjList[src]:
            if not self.dfs(neighbor, adjList, visit, path, topSort):
                return False
        path.remove(src)
        topSort.append(src)
        return True