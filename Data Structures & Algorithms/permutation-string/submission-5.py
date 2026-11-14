class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        s1_len = len(s1)
        s2_len = len(s2)

        al1 = [0]*26
        al2 = [0]*26

        if s1_len > s2_len:
            return False

        for c in range(s1_len):
            al1[ord(s1[c]) - ord("a")] += 1

        for r in range(s2_len):
            al2[ord(s2[r]) - ord("a")] += 1

            if r - left + 1 > s1_len:
                al2[ord(s2[left]) - ord("a")] -= 1
                left += 1
            if al1 == al2:
                return True


        return False
            


        


        