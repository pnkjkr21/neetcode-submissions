class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for i in nums:
            dic.setdefault(i, 0)
            dic[i] += 1
            if dic[i] > 1:
                return True
        return False
        