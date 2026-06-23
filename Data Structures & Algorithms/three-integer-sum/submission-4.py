class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        n=len(nums)
        for i in range(n-2):
            a=nums[i]
            if i > 0 and a == nums[i - 1]:
                continue
            if nums[n-1]<0 or a>0:
                break
            if nums[i]+nums[-1]+nums[-2]<0:
                continue
            
            left,right=i+1,n-1
            while left<right:
                threeSum=a+nums[left]+nums[right]
                if threeSum <0:
                    left+=1
                elif threeSum>0:
                    right-=1
                else:
                    ans.append([a,nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
        return ans
            
