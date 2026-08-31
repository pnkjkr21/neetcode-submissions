class Solution:
    # aaaaa
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        i = 0
        j = 0
        ans = 0
        while j < len(s):
            dic.setdefault(s[j], 0)
            dic[s[j]] += 1
            while dic[s[j]] > 1:
                dic[s[i]] -= 1
                i += 1
            ans = max(ans, j - i + 1)
            j += 1
        return ans

        