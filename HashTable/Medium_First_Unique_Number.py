"""
You have a queue of integers, you need to retrieve the first unique integer in the queue.
Implement the FirstUnique class:
1) FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
2) int showFirstUnique() returns the value of the first unique integer of the queue, and returns -1 if there is no such integer.
3) void add(int value) insert value to the queue.
 

Example 1:
Input: 
["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"]
[[[2,3,5]],[],[5],[],[2],[],[3],[]]
Output: 
[null,2,null,2,null,3,null,-1]

Explanation: 
FirstUnique firstUnique = new FirstUnique([2,3,5]);
firstUnique.showFirstUnique(); // return 2
firstUnique.add(5);            // the queue is now [2,3,5,5]
firstUnique.showFirstUnique(); // return 2
firstUnique.add(2);            // the queue is now [2,3,5,5,2]
firstUnique.showFirstUnique(); // return 3
firstUnique.add(3);            // the queue is now [2,3,5,5,2,3]
firstUnique.showFirstUnique(); // return -1

Example 2:
Input: 
["FirstUnique","showFirstUnique","add","add","add","add","add","showFirstUnique"]
[[[7,7,7,7,7,7]],[],[7],[3],[3],[7],[17],[]]
Output: 
[null,-1,null,null,null,null,null,17]

Explanation: 
FirstUnique firstUnique = new FirstUnique([7,7,7,7,7,7]);
firstUnique.showFirstUnique(); // return -1
firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7]
firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3]
firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3,3]
firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7,3,3,7]
firstUnique.add(17);           // the queue is now [7,7,7,7,7,7,7,3,3,7,17]
firstUnique.showFirstUnique(); // return 17

Example 3:
Input: 
["FirstUnique","showFirstUnique","add","showFirstUnique"]
[[[809]],[],[809],[]]
Output: 
[null,809,null,-1]

Explanation: 
FirstUnique firstUnique = new FirstUnique([809]);
firstUnique.showFirstUnique(); // return 809
firstUnique.add(809);          // the queue is now [809,809]
firstUnique.showFirstUnique(); // return -1

 
Constraints:
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^8
1 <= value <= 10^8
At most 50000 calls will be made to showFirstUnique and add.


Solution:
Use a dict to save the count of values and use a orderedDict to save the unique value with order
  when adding a value, check if it is in dict
    if not then add this value to both dict and orderedDict
    if it is in, then pop out this value from orderedDict (make orderedDict only saving unique value) and add its count+1 to dict
       notice this repeated value might have repeated before and been popped out before, so we need to set None as the default for pop()
  when showing the unique value
    if the orderedDict is None, then return -1
    else return the first key value in orderedDict, since it memorizes the order as oldest (which is the first unique value) to latest 

Complexity: Time O(N) (ignore hashing time and pop time, might not be strictly right) Space O(N)
"""

import collections
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.orderdict = collections.OrderedDict()  #use orderedDict to save the unique number in order
        self.dict = {}
        for num in nums: #must initialize, add each num as key in dict and orderdict
            self.add(num)
            
    def showFirstUnique(self) -> int:
        if len(self.orderdict)==0:
            return -1
        for key in self.orderdict.keys():
            return key #orderedDict memorize the order, the first key in dict is the first uniqe value

    def add(self, value: int) -> None:
        if value in self.dict: #repeat, not unique
            self.orderdict.pop(value, None) #pop out from orderdict once not unique, set None in case poped before 
            self.dict[value] += 1
        else:    #unique
            self.dict[value] = 1
            self.orderdict[value]=1
            


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)