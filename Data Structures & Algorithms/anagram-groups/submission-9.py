class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mp = {}
        results = []
        for s in strs:
            c = "".join(sorted(s))
            if c in mp:
                mp[c].append(s)
            else:
                mp[c] = [s]
        return list(mp.values())