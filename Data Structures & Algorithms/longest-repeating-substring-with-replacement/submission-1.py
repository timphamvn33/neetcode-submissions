class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # num_replacement = win_len - max_freq
        count = {}
        max_str_len = 0
        max_freq = 0
        max_len = 0
        left = 0

        for right in range(len(s)):
            # count the freq 
            count[s[right]] = count.get(s[right], 0) + 1

            # find the max frequence
            max_freq = max(max_freq, count.get(s[right]))
            win_len = right - left + 1

            if win_len - max_freq > k:
                count[s[left]] -= 1
                left += 1
            
            max_len = max(max_len, (right - left +1))
            
        
        return max_len
            

            





            