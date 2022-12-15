"""
https://leetcode.com/problems/concatenation-of-array/description/

in1
nums = [1,2,1]

out1
[1,2,1,1,2,1]

in2
[1,3,2,1]

out2
[1,3,2,1,1,3,2,1]
"""
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums+nums