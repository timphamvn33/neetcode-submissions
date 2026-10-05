class Solution:

    def encode(self, strs: List[str]) -> str:
        #combine string and put # between every strings
        a = ""
        for s in strs:
            a += f"{len(s)}#{s}"
        return a

    def decode(self, s: str) -> List[str]:
        # find the index of #
        i = 0
        result = []
        strs_len = len(s)
        while i < strs_len:
            j = i

            while s[j] != "#":
                j +=1
            # find the len of a string
            str_len = int(s[i:j])
            # use that length to determine and get the string
            str_start = j + 1
            str_end = j + str_len + 1
            result.append(s[str_start:str_end])
            # set a new i equal to the pointer at the str_end
            i = str_end
        return result


