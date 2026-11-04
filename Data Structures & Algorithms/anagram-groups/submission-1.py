class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # first we can sort the string element in the strs list then use it as a key in the hash map
        # list of anagram
        a_strs = []
        # hash_map of 
        str_map = {}

        for s in strs:
            s_sorted = "".join(sorted(s))
            if s_sorted in str_map.keys():
                str_map[s_sorted].append(s)
            else:
                str_map[s_sorted] = [s]
        return list(str_map.values())


            
            

        





















        # hash_map = defaultdict(list)
        # for str in strs:
        #     str_key_sorted = "".join(sorted(str))
        #     hash_map[str_key_sorted].append(str)
        # return list(hash_map.values())

