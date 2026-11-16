class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        results = []
        mp = {}

        for s in strs:
            a = [0]*26
            for c in s:
                a[ord(c) - ord("a")] += 1

            mp.setdefault(tuple(a), []).append(s)
        
        return list(mp.values())