class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # using depth-first-search to travel 4 directions
        # Time complexity will be O(row*col)
        count = 0
        def dfs(row, col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col]=="0":
                return
            # if grid[row][col] == 1, make it into 0 so we don't need to revisit
            grid[row][col] = "0"
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)

        # for using nested loops, call dfs function for every box having 1 then count ++
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i,j)
                    count += 1
        
        return count

        
