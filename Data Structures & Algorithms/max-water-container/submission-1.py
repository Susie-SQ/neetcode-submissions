class Solution:
    def maxArea(self, heights: List[int]) -> int:
        amount=0
        left,right=0,len(heights)-1
        while left<right:

            amount=max(amount,(right-left)*min(heights[left],heights[right]))
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return amount
                
