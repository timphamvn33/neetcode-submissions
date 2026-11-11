class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        
        strs_map = defaultdict(list)

        for s in strs:
            al = [0]*26
            for c in s:
                al[ord(c) - ord('a')] += 1

            strs_map[tuple(al)].append(s)

        return list(strs_map.values())




            
            

        





















        # hash_map = defaultdict(list)
        # for str in strs:
        #     str_key_sorted = "".join(sorted(str))
        #     hash_map[str_key_sorted].append(str)
        # return list(hash_map.values())

