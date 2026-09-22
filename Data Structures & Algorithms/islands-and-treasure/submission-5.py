class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows,cols=len(grid),len(grid[0])
        visit=set()
        q=deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    q.append([r,c])
                    visit.add((r,c))
            
        def dfs(r,c):
            if min(r,c)<0 or r ==rows or c ==cols or (r,c) in visit or grid[r][c]==-1:
                return
            q.append([r,c])
            visit.add((r,c))
        dis=0
        while q:
            for i in range(len(q)):
                r,c=q.popleft()
                grid[r][c]=dis
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)
            dis+=1