class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, ans =0,0
        dic = {}
        for r,c in enumerate(s):
            l = max(l, dic.get(c, -1)+1)
            dic[c] = r
            ans = max(ans, r - l +1)
        return ans