class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic = {}
        temp = {}
        for i in s1:
            dic.setdefault(i, 0)
            dic[i] += 1
        
        i, j = 0, 0
        while j < len(s2):
            if s2[j] not in dic:
                temp = {}
                j += 1
                i = j
                continue
            elif s2[j] in dic:
                temp.setdefault(s2[j], 0)
                temp[s2[j]] += 1
                while temp[s2[j]] > dic[s2[j]]:
                    temp[s2[i]] -= 1
                    i += 1
                if self.approved(dic, temp):
                    return True
            j += 1
        return False
    
    def approved(self, dic, temp):
        if len(dic) == len(temp):
            for i in dic:
                if dic[i] != temp[i]:
                    return False
            return True
        return False
            
        