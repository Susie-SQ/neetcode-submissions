class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        res=0
        q=deque()
        rows,cols=len(grid),len(grid[0])
        fresh=0#这里有2表明状态了，而不是需要自己去set
        for m in range(rows):
            for n in range(cols):
                if grid[m][n]==2:
                    q.append([m,n])
                elif grid[m][n]==1:
                    fresh+=1
        def dfs(m,n):
            #nonlocal
            nonlocal fresh
            if min(m,n)<0 or m==rows or n==cols or grid[m][n]!=1:
                return
            q.append([m,n])
            fresh-=1
            grid[m][n]=2#表明已腐烂
        while q and fresh>0:
            for i in range(len(q)):
                r,c=q.popleft()
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)
            res+=1
        if fresh==0:
            return res
        return -1