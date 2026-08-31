class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dic_t = {}
        dic_s = {}
        for i in t:
            dic_t.setdefault(i, 0)
            dic_t[i] += 1
        
        have = 0
        req = len(dic_t)
        l, m = 0, len(s)
        length = float('inf')
        ans = ''

        for i in range(len(s)):
            dic_s.setdefault(s[i], 0)
            dic_s[s[i]] += 1
            
            if s[i] in dic_t and dic_t[s[i]] == dic_s[s[i]]:
                have += 1
                while have == req:
                    if length > i - l + 1:
                        length = i - l + 1
                        ans = s[l:i+1]
                    dic_s[s[l]] -= 1
                    if s[l] in dic_t and dic_s[s[l]] < dic_t[s[l]]:
                        have -= 1
                    l += 1
        return ans

        