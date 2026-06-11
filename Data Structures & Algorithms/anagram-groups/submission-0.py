class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic=defaultdict(list)
        for x in strs:
            sort_x=''.join(sorted(x))
            dic[sort_x].append(x)
        return list(dic.values())