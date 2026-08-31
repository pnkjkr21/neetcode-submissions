class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = {}
        ans = 0
        l = 0
        for r in range(len(s)):
            dic.setdefault(s[r], 0)
            dic[s[r]] += 1

            while (r - l + 1) - max(dic.values()) > k:
                dic[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans
                
                


        