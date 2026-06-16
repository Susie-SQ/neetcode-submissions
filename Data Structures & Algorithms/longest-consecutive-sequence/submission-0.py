class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans=t=0
        for x in nums:
            while x-1 in nums:
                t+=1
                x=x-1
            ans=max(ans,t+1)
            t=0
        return ans