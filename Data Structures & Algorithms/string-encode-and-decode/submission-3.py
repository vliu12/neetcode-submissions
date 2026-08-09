class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += word + "}}"
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        for word in s.split("}}"):
            res.append(word)
        res.pop() # for last whitespace
        return res