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
# 5. If at any point while processing, if idle time becomes negative, then stop (meaning there's no idle slots for CPU). the result is just the length of tasks
# 6. If not at the end, the result is length of tasks + number of idle slots


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

    
 

# APPROACH 2: Greedy solution (CLASS) 
# Time Complexity : O(n), n: length of tasks
# Space Complexity : O(1), size of hashmap constant as it can have only A-Z, 26 constant size
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : None
#
#
# Your code here along with comments explaining your approach
# 1. Same intuition as above. 
# 2. Number of partition (ie., empty slots) will be maximum frequency of the task - 1. (blank spaces between tasks). 
# 3. To get total length of empty slots => number of partitions * (n - number of tasks having frequency as the maximum frequency + 1)
# 4. To get the remaining pending tasks (after considering tasks with maximum frequency), length of tasks (total number of tasks) - (number of tasks having frequency as the 
#    maximum frequency * maximum frequency)
# 5. To get idle time => length of empty slots - reminainig pending tasks

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        if tasks is None or len(tasks) < 1:
            return 0
        
        hashmap_freq, maxFreq = defaultdict(int), 0
        for char in tasks:
            hashmap_freq[char] += 1
            maxFreq = max(maxFreq, hashmap_freq[char])
            
        maxFreqTasks = 0
        for key in hashmap_freq:
            if hashmap_freq[key] == maxFreq:
                maxFreqTasks += 1
            
        num_partitions = maxFreq - 1
        num_empty_slots = num_partitions * (n - maxFreqTasks + 1)
        num_pending_tasks = len(tasks) - (maxFreq * maxFreqTasks)
        idle_slots = max(0, num_empty_slots - num_pending_tasks)
        
        CPU_time = len(tasks) + idle_slots
        
        return CPU_time
