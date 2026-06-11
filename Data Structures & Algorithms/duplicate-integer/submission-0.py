class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic=defaultdict(int)
        for i in nums:
            dic[i]+=1
            if dic[i]>1:
                return True
        return False