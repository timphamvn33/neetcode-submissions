class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mp = defaultdict(list)
        results = []
        for s in strs:
            c = "".join(sorted(s))
            mp[c].append(s)
        return list(mp.values())