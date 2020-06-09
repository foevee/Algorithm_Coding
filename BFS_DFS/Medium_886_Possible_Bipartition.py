"""
Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.
Each person may dislike some other people, and they should not go into the same group. 
Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.
Return true if and only if it is possible to split everyone into two groups in this way.

Example 1:
Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4], group2 [2,3]

Example 2:
Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false

Example 3:
Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false
 

Note:
1 <= N <= 2000
0 <= dislikes.length <= 10000
1 <= dislikes[i][j] <= N
dislikes[i][0] < dislikes[i][1]
There does not exist i != j for which dislikes[i] == dislikes[j].


Method: graph bipartition, use either DFS or BFS

1. General Theory
The question asks us to divide given people into two groups such that no two people in the same group dislike each other.

For ease of understanding, we can represent this problem as a graph, with people being the vertices and dislike-pairs being the edges of this graph.
We have to find out if the vertices can be divided into two sets such that there aren't any edges between vertices of the same set. A graph satisfying this condition is called a bipartite graph. 

We try to group the two sets of vertices, with 1 and -1 ids. In a bipartite graph, the 1(id) vertex must be connected only with -1(id)vertices. In other words, there must NOT be any edge connecting two vertices of the same id. Such an edge will be a conflict edge.

The presence of conflict edges indicate that bipartition is NOT possible.

2. Solution
The graph may consist of many connected components. For each connected component, we run our BFS/DFS algorithm to find conflict edges, if any. For each component, we start by grouping one vertex 1(id), and all it's neighbours -1(id). Then we visit the -1(id) vertices and group all their neighbours as 1(id), and so on. During this process, if we come across any same-id edge, we have found a conflict edge and we immediately return false, as bipartition will not be possible.

If no conflict edges are found at the end of the algorithm, it means bipartition is possible, hence we return true.

Complexity:
Time O(V+E) (all vertices + edges are visted once)
Space O(V+E) (need to save all vertices and edges)
"""

#method 1: DFS (use another function to recursively check and group id for each vertex number)
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        if not dislikes:
            return True
		# initialize
        # use a dict of list to save each dislikes neighbors of a number
        neighbor = {}
        for a,b in dislikes:
            #change 1~N number to index 0~N-1
            neighbor[a-1] = neighbor.get(a-1,[])+[b-1]
            neighbor[b-1] = neighbor.get(b-1,[])+[a-1]
        
        #use a list to represent each number's assigning group(-1,1), init to 0 means not-assigned yet
        group = [0 for i in range(N)]
        
        for i in range(N):
            if group[i]!=0: #already visited and assigned
                continue
            if not self.dfs_group(neighbor, group, i, 1):
                return False
        return True
    
    def dfs_group(self, neighbor, group, k, group_id):
        if group[k]!=0: #if already grouped, check if the id is the same as desired (assigned)
            return group[k]==group_id 
        group[k] = group_id #1 or -1

        for i in neighbor.get(k,[]): #always use get in case the key not in dict
            if not self.dfs_group(neighbor, group, i, -group_id): #not grouped, group to new id (converse)
                return False
        return True


#method 2: BFS (use a queue loop to visit each vertex number and push its neighbor in to check)
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        if not dislikes:
            return True
        # use a dict of list to save each dislikes neighbors of a number
        neighbor = {}
        for a,b in dislikes:
            #change 1~N number to index 0~N-1
            neighbor[a-1] = neighbor.get(a-1,[])+[b-1]
            neighbor[b-1] = neighbor.get(b-1,[])+[a-1]
        
        #use a list to represent each number's assigning group(-1,1), init to 0 means not-assigned yet
        group = [0 for i in range(N)]
        queue = [] #use queue to do BFS
        
        #use another list to track if visited this number in the BFS-queue loop
        visited = [False for i in range(N)] 
        #This is different from group[i]!=0, since when we assign an id and append the number, we have grouped the id but not visit it and its neighbor during the BFS-queue loop yet
        for i in range(N):
            if visited[i]!=0: #already visited (notice even group[i]!=0 still might not been visited)
                continue
            group[i] = 1
            queue.append(i)
            while(queue):
                k = queue.pop(0)
                if visited[k]:  #already visited
                    continue
                visited[k] = True
                for j in neighbor.get(k,[]):
                    if group[j]!=0 and group[j]==group[k]: #once same-id edge appears, return False
                        return False
                    if group[j]==0:
                        group[j] = -group[k]
                    queue.append(j) #add to the end of the queue (but might note been visited before)
        
        return True
                
            
        