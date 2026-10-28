class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_list = [0]*26
        s2_list = [0]*26
        s1_len = len(s1)
        s2_len = len(s2)

        if s1_len > s2_len:
            return False

        for n in range(s1_len):
            s1_list[ord(s1[n]) - ord("a")] += 1
            s2_list[ord(s2[n]) - ord("a")] += 1

        if s1_list == s2_list:
            return True
        for right in range(s1_len, s2_len):
            # count the char in s2
            s2_list[ord(s2[right])- ord("a")] += 1
            # minus the char at the pointer left when the window moves
            s2_list[ord(s2[right-s1_len])- ord("a")] -= 1
            
            if s2_list == s1_list:
                return True
        return False