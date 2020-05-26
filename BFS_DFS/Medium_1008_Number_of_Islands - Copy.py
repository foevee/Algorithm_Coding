"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input:
11110
11010
11000
00000
Output: 1

Example 2:
Input:
11000
11000
00100
00011
Output: 3


Solution: 
Use Depth First Search to find all connected islands at each time
  we only use DFS to visit island with "1" and each time mark the visited island as "-1" so it will not be revisited 
  each time we visited all the connected island group and count+=1
  loop through the whole array while using DFS to get the count, which is the connected island (group) number
"""


def DFS(grid, x, y):
    m = len(grid)
    n = len(grid[0])
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    if grid[x][y]!='1' or x<0 or x>=m or y<0 or y>=n:
        return
    grid[x][y]='-1'  #mark visited island as '-1'
    for i in range(4):  #check all 4 directions to check connected islands (within the same group)
        new_x = x+dx[i]
        new_y = y+dy[i]
        if(new_x<0 or new_x>=m or new_y<0 or new_y>=n):
            continue
        if(grid[new_x][new_y]=='1'):
            DFS(grid, new_x, new_y)
    return
    
def numIslands(grid: List[List[str]]) -> int:  
    if not grid:  ##must add boundary check in case corner case grid == [] (then grid[0] will raise error)
        return 0
    m = len(grid)
    n= len(grid[0])
    count = 0
    for i in range(m):
        for j in range(n):
            if(grid[i][j]=='1'):
                DFS(grid, i, j)
                count += 1
    return count