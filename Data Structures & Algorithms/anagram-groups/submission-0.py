class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # first we can sort the string element in the strs list then use it as a key in the hash map
        hash_map = defaultdict(list)
        for str in strs:
            str_key_sorted = "".join(sorted(str))
            hash_map[str_key_sorted].append(str)
        return list(hash_map.values())

