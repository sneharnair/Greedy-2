# APPROACH 1: Greedy Solution
# Time Complexity : O(n), n: length of ratings
# Space Complexity : O(1), not including space of result array
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : None
#
#
# Your code here along with comments explaining your approach
# 1. Initialize result array to 1 for every ind as all children must get atleast one candy.
# 2. For every ind compare it's rating to it's left neighbor, if greater, then assign one more than the candy of it's left neighbor to the current index. 
# 3. Then, for evety index, compare it's rating to it's right neighbor, if greater, check if it's candy is more than that of it's right neighbor. 
#                                                                                   -> if Yes, do nothing (we need to assign only min candies)
#                                                                                   -> if No, then assign one more than the candy of it's right neighbor. 


class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        if len(ratings) < 1 or ratings is None:
            return 0
        
        result = [1 for _ in range(len(ratings))]
        
        # check with left neighbor
        for ind in range(1, len(ratings)):
            if ratings[ind] > ratings[ind - 1]:
                result[ind] = result[ind - 1] + 1
                
        # check with right neighbor
        for ind in range(len(ratings) - 2, -1, -1):
            if ratings[ind] > ratings[ind + 1] and result[ind] <= result[ind + 1]:
                result[ind] = result[ind + 1] + 1
        
        return sum(result)
        
