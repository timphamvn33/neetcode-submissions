class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)

        # brute-force solution
        for i in range(s2_len):
            if sorted(s2[i: i+s1_len ]) == sorted(s1):
                return True
        return False
            

        