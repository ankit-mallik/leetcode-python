class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = -1
        maximum = 0

        for i in range(len(nums)):
            if nums[i] != 1:
                l = i
            else:
                maximum = max(i - l, maximum)
        return maximum
        