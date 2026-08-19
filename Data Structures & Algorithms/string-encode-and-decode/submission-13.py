class Solution:

    def encode(self, strs: List[str]) -> str:
        delimiters = [0]
        for i in strs:
            delimiters.append(delimiters[-1]+len(i))
        if len(strs) > 0:
            res = "1["
            for i in delimiters:
                res += str(i)
                res += ","
            res += "]"
            res += "".join(strs)
            return res
        else:
            return "0"

    def decode(self, s: str) -> List[str]:
        if len(s) == 1 and s == '0':
            return []
        s = s[1:]
        i = 0
        while s[i] != "]":
            i += 1
        indexes = s[1:i-1]
        indexes = list(map(int, indexes.split(',')))
        s = s[i+1:]
        last = 0
        res = []
        for i in indexes:
            res.append(s[last:i])
            last = i
        return res[1:]

