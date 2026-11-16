class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_join = "".join(c for c in s if c.isalnum())
        left, right = 0, len(s_join) -1
        while left < right:
            if s_join[left].lower() != s_join[right].lower():
                return False
            left += 1
            right -= 1
        return True






        
