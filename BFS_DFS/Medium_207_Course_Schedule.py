"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
 
Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.

Solution: DFS/BFS

We can use either DFS or BFS to achieve the search of each course (and its neighbors)

# Method 1: DFS
Treat this problem as graph search, init each course as a node, with neighbors as its prerequisites, and then search each course i and its neighbors to see if there are any cycles. If yes, then we can not finish since cycle requires each other to be prerequisite. If not, we mark this course i as finished visiting and go to next unfinished course. During the loop of searching every course, if any course get a subcycle during search, we return false; otherwise if all courses finished visting without any subcycles, we return True.

Notice we must distinguish the visit of a course i with 2 scenarios: 
1) during visit the neighbor of course i, return to this node i => cylce (return false)
2) it has been finished visiting before without any cycle, now we meet this node i as a neighbor of another course j (while visiting j), we should not mark this as cycle but should just jump over it

We use two mark number to distinguish: 
when starting visiting course i and its neighbor, we mark visited[i]=-1 (means starting visit)
   thus when 1) happened, we get visited[i]==-1, we should return false
After finishing visiting i without any cycle (return false), we mark visited[i]=1 (means finished visiting)
   thus when 2) happend, we get visited[i]==1, we should return true (as jump over during the process, as we only return True finally when all courses have been visited without any false return)


# Method 2: BFS (with Topological sort)
2. If use BFS, we must only visit from those courses (nodes) with in-degrees==0, otherwise we can not find the correct way to visit each node and detect the true cycle without being affected by re-visiting (thus detect false cycle) or incomplete visiting (thus fail to detect true cycles)
- First try to find a node with 0 indegree, set total visiting time n = # of courses (numCourses)
  - If we fail to do so, there must be a cycle in the graph and we return false. 
- Otherwise then we will get a queue (list) of courses with in-degrees = 0, we will loop through this queue to visit each starting course
  - At each round, decrease the total visiting time by 1, and use a further inner loop to visit all its neighbors
    At the inner loop, reduce the indegrees of its neighbors by 1 and add the neighbors with now in-degree=0 to the queue
- If successfully (no cycle and visiting all courses), this process should be repeated for n times, which means at the end n==0 
so return true for n==0 and false otherwise
(The above method is indeed the topological sort)

----------------------------------------------------------------------------------------
**Topological Sort**
In computer science, a topological sort or topological ordering of a directed graph is a linear ordering of its vertices such that for every directed edge uv from vertex u to vertex v, u comes before v in the ordering.
https://en.wikipedia.org/wiki/Topological_sorting

[Kahn's algorithm]
First, find a list of "start nodes" which have no incoming edges and insert them into a set S; at least one such node must exist in a non-empty acyclic graph. Then:

L ← Empty list that will contain the sorted elements
S ← Set of all nodes with no incoming edge

while S is not empty do
    remove a node n from S
    add n to tail of L
    for each node m with an edge e from n to m do
        remove edge e from the graph
        if m has no other incoming edges then
            insert m into S

if graph has edges then
    return error   (graph has at least one cycle)
else 
    return L   (a topologically sorted order)
----------------------------------------------------------------------------------------


Notice when starting from courses with in-degrees>0, that is not feasible since this course still has pre-requisites. We must start from 0 in-degree course i. We use a queue to initialize with all courses with 0 in-degrees and loop through the queue to visit it. At each round, we pop out the queue front course i and decrease the visiting time by 1 (as just finished this course). Then we use a inside loop to visit all its neighboring (next) course j and decrease that course's in-degree by 1 (degree-=1) to remove out this path (i-j path). If the neighbor now has the in-degree=0, it can be the new start point (i.e. to visit its next_ courses), so we push it to the queue. Keep following this trend and visit the neighboring course of j. In the end, we should have visiting time n == 0 after looping through all the queue (now queue is empty). Otherwise we get the cycle so that we can not finish visiting all the courses before exit, so we return false.


Complexity: (both BFS/DFS) Time O(E+V) Space O(E+V) 

**!!!**
- Notice if use DFS, we can start from any course id and use DFS function to recursively visit its neighbor and get correct result.
However for BFS, although the logic is almost the same, we process differently, must start from courses with in-degrees = 0.
- This is becauses DFS use a outer helper function to do recursion, which can recursively find the nodes with 0 in-degress and start, making sure the graph visit is indeed successfully (with right start) without affecting detecting false cycle due to wrong starting point.
- While BFS only use the same function with a queue to loop each course (node) and its neighbor, once the starting point does not have 0 in-degree, it might not fininsh visiting all nodes (some not being visited fully of all neighbors before being marked as visited as the neighbor of visting another source node), thus failing to detect true cycles. This is also wrong since we can not start learning a course without studying its pre-requists first. So we can only start from those courses with 0 in-degrees.
**!!!**
"""


# Method 1: DFS (use visited[i]==1 or -1 to check finished or sub-cycle)
# we can start from any course (node) and use another helper function (DFS) to recursively visit the nodes and their neighbors, without worrying about not fully visiting all the nodes
class Solution:  
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = {}
        visited = [0 for i in range(numCourses)]
        if not prerequisites:
            return True
        #initialize
        for a,b in prerequisites:
            pre[a] = pre.get(a,[])+[b]
        
        for i in range(numCourses):
            if not self.DFS(i, pre, visited):
                return False
        return True
    
    def DFS(self, course_i, pre, visited):
        if visited[course_i] in {1,-1}:
            return visited[course_i]==1 #return true for 1 (finished visiting before) false for -1 (sub-cycle)
        
        visited[course_i] = -1 #mark as initial visited
        #now check if we would go back to course_i (meet a ring) staring from its neighbor
        for j in pre.get(course_i,[]): #loop its next courses
            if not self.DFS(j, pre, visited): #each next_course require dfs
                return False
        #mark as finish visit succuss (no cycle)
        visited[course_i] = 1
        return True
            

# Method 2 (Optimal): BFS (with Topological sort)
# must start visiting from courses (nodes) with in-degrees==0, use a queue to save all courses with 0 in-degrees and visit
# This is indeed the topological sort, we start from the node with the least topological degree, and visit its neighbor one by one, once finished visiting one, we decrease its degree by 1, and push back any new nodes with the new in-degree = 0 to the queue. Keep following the topological order to visit all the nodes until exit (finished visiting).

# Our method here is indeed using the topological sort idea with [Kahn's algorithm] (see above)
# All the nodes in the start_course queue is pushed following their topologigcal order (in-degrees ascendingly)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        next_ = {} #save the next course of each pre-requisite course
        degree = [0 for i in range(numCourses)] #in-degree of each course (node)
        n = numCourses #mark the # of courses need to be visited
        start_course = []
        
        if not prerequisites:
            return True
        #initialize
        for a,b in prerequisites:
            next_[b] = next_.get(b,[])+[a]
            degree[a] += 1
            
        #find the course with in-degree = 0
        for i,k in enumerate(degree):
            if k==0: 
                start_course.append(i)
        if not start_course:
            return False  #no in-degree=0, must have cycle
        
        while(start_course):
            k = start_course.pop(0)
            n -= 1
            for j in next_.get(k,[]):
                degree[j] -= 1
                if degree[j] == 0:
                    start_course.append(j)
        #if finally we do not visit all the courses (n==0), we must encounter some cycle and thus can not visit all courses (return false)
        return n==0 
                