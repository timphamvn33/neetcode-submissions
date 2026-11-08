class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        if not s:
            return 0
        else:
            set_s = set()
            left = 0
            result = 0

        for n in range(len(s)):

            while s[n] in set_s:
                set_s.remove(s[left])
                left += 1
            set_s.add(s[n])
            result = max(result, len(set_s))
        return result






        
        