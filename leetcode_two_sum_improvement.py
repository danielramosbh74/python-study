"""
This example was based on the user "panahi", Clean Python One-Pass solution,
in Leetcode.

The only improvement is the more detailed comment, 
that shows how to use this code in Jupyter Notebook / Google Colab,
command line or in another IDE (ex. VSCode)
"""

list = readline()
for item in list:
    print(item

"""
list = [1, 23, 45, 0, 9]
for item in list:
    print(item)
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        """
        IMPORTANT:
        If you're running this code at the command line or 
        other IDE rather than Leetcode, 
        you must uncomment the 3 lines below to allow data input
        """
       
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        """
        Example 1:
        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        Output: Because nums[0] + nums[1] == 9, we return [0, 1].
        
        Example 2:
        Input: nums = [3,2,4], target = 6
        Output: [1,2]
        """
    
        seen = {}
        for i, v in enumerate(nums):
            remaining = target - v
            if remaining in seen:
                return [seen[remaining], i]
            seen[v] = i
        return []

