class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visit, path = set(), set()
        crsList = []

        def dfs(crs):
            if crs in path: return False
            if crs in visit: return True

            path.add(crs)
            visit.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre): return False
            path.remove(crs)
            crsList.append(crs)
            return True
        
        for c in range(numCourses):
            if not dfs(c): return []
        return crsList