class Solution:
    def findMin(self, nums: List[int]) -> int:
        mini=float("inf")
        for x in nums:
            if x<mini:
                mini=x
        return mini
