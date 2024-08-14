from collections import deque 

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid) # get the number of rows
        if rows == 0:
            # grid is empty
            return -1
        
        cols = len(grid[0]) # get the number of cols
        fresh_oranges = 0 # counter for fresh oranges
        rotten = deque() # queue with rotten oranges (for bfs)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append((r,c)) # add the rotten orange coordinates to the queue
                elif grid[r][c] == 1:
                    fresh_oranges += 1

        # keep track of minutes passed
        minutes = 0

        while rotten and fresh_oranges > 0:
            minutes += 1 # update the number of minutes passed

            for _ in range(len(rotten)):
                x, y = rotten.popleft()

                # visit all the adjacent cells
                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    xx, yy = x + dx, y + dy

                    if xx < 0 or xx == rows or yy < 0 or yy == cols:
                        # ignore cell if it's out of the grid boundary
                        continue
                    
                    if grid[xx][yy] == 0 or grid[xx][yy] == 2:
                        # ignore cell if it's empty(0) or visited before(2)
                        continue
                    
                    fresh_oranges -= 1 # update the fresh orange counter
                    grid[xx][yy] = 2 # mark the current orange as rotten
                    rotten.append((xx, yy)) # add the current rotten to the queue
        
        return minutes if fresh_oranges == 0 else -1
            
