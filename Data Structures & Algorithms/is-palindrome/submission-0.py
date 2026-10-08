class Solution:
    def isPalindrome(self, s: str) -> bool:
        # using 2 pointers left and right to check if the left and right char equal
        join_string = "".join(char for char in s if char.isalnum())
        left = 0
        right = len(join_string) -1
        while left < right:
            if join_string[left].lower() != join_string[right].lower():
                return False
            left +=1
            right -= 1
        return True
        