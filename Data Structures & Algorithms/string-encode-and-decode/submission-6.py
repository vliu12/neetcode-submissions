class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            num = len(word)
            res = res + str(num) + "#" + word 
        
        print(res)

        return res

    def decode(self, s: str) -> List[str]:
        out = []
        i = 0
        while i < len(s):
            len_word = ""
            while s[i] != "#":
                len_word += s[i]
                i += 1
            len_word = int(len_word)
            print(len_word)
            i += 1
            curr = ""
            while len_word > 0:
                curr += s[i]
                i += 1
                len_word -= 1
                

            out.append(curr)

        return out


            
