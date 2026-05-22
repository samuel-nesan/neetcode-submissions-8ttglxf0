class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visit, path = set(), set()

        def dfs(crs):
            if crs in path: return False
            if crs in visit: return True

            visit.add(crs)
            path.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre): return False
            path.remove(crs)
            return True
        
        for c in range(numCourses):
            if not dfs(c): return False
        return True
        