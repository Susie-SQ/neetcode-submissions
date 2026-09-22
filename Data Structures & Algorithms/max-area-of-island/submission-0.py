class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        ans=0
        sumNum=0
        def dfs(i,j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]!=1:
                return
            nonlocal sumNum
            sumNum+=1
            grid[i][j]=2
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        for i,row in enumerate(grid):
            for j,col in enumerate(row):
                if grid[i][j]==1:
                    sumNum=0
                    dfs(i,j)

                    ans=max(ans,sumNum)
        return ans