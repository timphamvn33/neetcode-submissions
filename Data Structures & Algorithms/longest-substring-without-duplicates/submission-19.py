class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        set_s = set()
        result = 0

        for r in range(len(s)):
            while s[r] in set_s:
                set_s.remove(s[left])
                left += 1
            
            set_s.add(s[r])

            result = max(result, r - left + 1)
        return result








        
        