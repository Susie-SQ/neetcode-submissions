class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count1 = Counter(s1)
        count2 = Counter()
        for i,c in enumerate(s2):
            count2[c] += 1
            if i < len(s1) - 1:
                continue
            if count2 == count1:
                return True
            count2[s2[i-len(s1)+1]] -= 1
            #s2[]
        return False

