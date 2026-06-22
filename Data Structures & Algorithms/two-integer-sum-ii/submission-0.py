class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans=[]
        num=defaultdict(int)
        for i,x in enumerate(numbers):
            if target-x in num:
                return [num[target-x]+1,i+1]
            num[x]=i

