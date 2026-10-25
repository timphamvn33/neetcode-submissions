class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_set = set()
        left = 0
        max_win_len = 0
        for n in range(len(s)):
            right = n
            while s[right] in my_set:
                my_set.remove(s[left])
                left +=1
                
            my_set.add(s[right])

            curr_win_len = right - left + 1
            max_win_len = max(max_win_len, curr_win_len)
        
        return max_win_len


            
