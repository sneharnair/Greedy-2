# APPROACH 1: Greedy solution
# Time Complexity : O(n), n: length of tasks
# Space Complexity : O(1), size of frequency array id constant as it can have only A-Z, 26 constant size
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : None
#
#
# Your code here along with comments explaining your approach
# 1. Main intuition: CPU time is busy time + idle time. busy time is length of tasks. Need to determine the idle time because of cooldown
# 2. Idle time is mainly bottlenecked by the tasks with maximum frequency. Thus, initally the max possible idle time is (number of time units of cooldown) * (max frequency - 1).
#    Place the task with max frequency at proper spaced out with n so the number of idle slots (is the blank spaces between tasks) so max frequncy -1 and those slots will be of 
#    length same as n. 
# 3. Get the frequency of all tasks and sort them in descending order. 
# 4. now for each task decrease the idle time by minimum of (maximum frequency -1 -> when we have more than one task of same maximum frequency, current frequency)
# 5. If at any point while processing


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        if tasks is None or len(tasks) < 1:
            return 0
        
        freq = [0 for _ in range(26)]
        for char in tasks:
            freq[ord(char) - ord("A")] += 1
            
        freq.sort()
        maxFreq = freq.pop()
        idle_time = n * (maxFreq - 1)
        
        for ind in range(len(freq) - 1, -1, -1):
            idle_time -= min(maxFreq - 1, freq[ind])
            if idle_time < 0:
                break
        
        idle_time = max(0, idle_time)
        return len(tasks) + idle_time
