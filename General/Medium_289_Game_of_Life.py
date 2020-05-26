"""
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:
Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]

Follow up:
Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?


Solution:
Use a 2D array to loop through each cell and check state according to its neightbor, then re-loop again to update its state
Complexity: Time O(N^2) Space O(N^2)

"""
import copy
def gameOfLife(self, board):
    """
    :type board: List[List[int]]
    :rtype: None Do not return anything, modify board in-place instead.
    """
    neighbors=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
    #To use in-place change and distinguish original 0&1, here -1 for die and 2 for live
    live_rules=[-1,-1,1,1,-1,-1,-1,-1,-1] # 0-9 ways of living neighbors
    dead_rules=[0,0,0,2,0,0,0,0,0]
    state_before_chg={0:0,1:1,2:0,-1:1} #2: from death(0)->live; -1 from live(1) to death
    chg_to_state={0:0,1:1,2:1,-1:0}
        
    m,n=len(board),len(board[0])
    for i in range(m):
        for j in range(n):
            total=sum([state_before_chg[board[i+p][j+q]] for p,q in neighbors if 0<=i+p<m and 0<=j+q<n])
            board[i][j]=live_rules[total] if board[i][j]==1 else dead_rules[total]
    for i in range(m):
        for j in range(n):
            board[i][j]=chg_to_state[board[i][j]]
        
