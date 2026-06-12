class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt=defaultdict(int)
        ans=[]

        for x in nums:
            cnt[x]+=1

        items = sorted(cnt.items(), key=lambda x: x[1], reverse=True)
        for i in range(k):
            ans.append(items[i][0])

        return ans