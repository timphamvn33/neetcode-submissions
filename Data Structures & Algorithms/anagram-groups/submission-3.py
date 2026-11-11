class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        strs_map = {}
        for s in strs:
            x = "".join(sorted(s))
            strs_map[x] = strs_map.get(x, [])
            strs_map[x].append(s)
        return list(strs_map.values())




            
            

        





















        # hash_map = defaultdict(list)
        # for str in strs:
        #     str_key_sorted = "".join(sorted(str))
        #     hash_map[str_key_sorted].append(str)
        # return list(hash_map.values())

