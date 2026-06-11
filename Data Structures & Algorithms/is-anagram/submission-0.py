class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic1=defaultdict(int)
        dic2=defaultdict(int)
        for i in s:
            dic1[i]+=1
        for i in t:
            dic2[i]+=1
        if dic1 != dic2:
            return False
        return True