class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        strs_map = {}
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s not in strs_map:
                strs_map[sorted_s] = [s]
            else:
                strs_map[sorted_s].append(s)
        return list(strs_map.values())