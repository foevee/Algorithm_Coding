class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ##Time: O(m*n)  Space: O((m+1)*(n+1))
        m,n=len(grid),len(grid[0])
        Path=[[float('inf')]*(n+1)]*(m+1) #extra padding top and left to allow dynamic programming
        Path[1][1]=grid[0][0] #Initialize
        for i in range(1,m+1):
            for j in range(1,n+1):
                if i==1 and j==1:
                     continue
                Path[i][j]=min(Path[i][j-1],Path[i-1][j])+grid[i-1][j-1] 
                #remember in grid still has m*n shape, notice index!
        
        return Path[m][n]
    
    
    #Better Way:
    #Space Complexity: O(1)
    """
    public int minPathSum(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        for(int i = 1;i<n;i++){
            grid[0][i] += grid[0][i-1];
        }
        for(int i = 1;i<m;i++){
            grid[i][0] += grid[i-1][0];
            for(int j = 1;j<n;j++){
                grid[i][j] += Math.min(grid[i][j-1],grid[i-1][j]);
            }
        }
        return grid[m-1][n-1];
    }
    
    """