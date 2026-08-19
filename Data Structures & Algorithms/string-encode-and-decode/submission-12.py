class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) > 0:
            if len('-'.join(strs)) > 0:
                return '1'+'thalaforareason'.join(strs)
            else:
                return '1'+""
        else:
            return "0"

    def decode(self, s: str) -> List[str]:
        if len(s) == 1 and s == '0':
            return []
        return s[1:].split('thalaforareason')
