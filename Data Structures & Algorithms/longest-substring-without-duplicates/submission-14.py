class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        if not s:
            return 0
        else:
            set_s = set()
            left, right = 0, 0
            result = 0

            while right < len(s):
                if s[right] not in set_s:
                    set_s.add(s[right])
                    right += 1
                    result = max(result, len(set_s))
                else:
                    set_s.remove(s[left])
                    left += 1
            return result







        
        