class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # we're gonna use hash map to solve this problem by counting the words in s and compare with t

        # initialze hash map to count s and count t
        count_s = {}
        count_t = {}

        # check if the length of s is different with the length of t then we return false
        if len(s) != len(t):
            return False
        
        # set the keys and values into the count_s. keys are characters and values are the number of times of that characters appearing in that string
        for c in s:
            count_s[c] = count_s.get(c, 0) + 1
        
        # iterate the t string and then minus the count of the character from the count_s hash map
        for c in t:
            count_s[c] = count_s.get(c, 0) -1

        # iterate the count_s hash map to chek whether we have any value is not zero then return false
        for cs in count_s.values():
            if cs != 0:
                return False
        
        return True
