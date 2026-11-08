class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Base case: an empty string has a maximum substring length of 0
        if not s:
            return 0
            
        long_s = set()
        left, right = 0, 0  # Start both pointers at 0 to evaluate the first character
        long_max = 0
        
        while right < len(s):
            if s[right] not in long_s:
                long_s.add(s[right])
                right += 1
                long_max = max(long_max, len(long_s))
            else:
                # Shrink the window from the left until the duplicate is removed
                long_s.remove(s[left])
                left += 1
                
        return long_max
