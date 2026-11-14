class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        s_set = set()

        for n in range(len(s)):
            

            while s[n] in s_set:
                s_set.remove(s[left])
                left += 1
            s_set.add(s[n])
            max_len = max(max_len, n-left + 1)
        return max_len








        
        