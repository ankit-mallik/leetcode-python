class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seek = set()
        for num in nums:
            if num not in seek:
                seek.add(num)
            else:
                return True
        return False