class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for i,x in enumerate(nums):
            if target-x in dic:
                return [dic[target-x],i]
            dic[x]=i
            