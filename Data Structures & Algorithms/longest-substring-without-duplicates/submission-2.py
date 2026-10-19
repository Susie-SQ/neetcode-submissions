class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cnt = defaultdict(int)
        ans = left = 0
        for i,x in enumerate(s):
            cnt[x] += 1
            while cnt[x] > 1:
                cnt[s[left]] -= 1
                left += 1
            ans = max(ans, i - left + 1)
        return ans