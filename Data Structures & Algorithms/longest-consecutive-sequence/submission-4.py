class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = {}
        ans = 0
        for num in nums:
            if num in dic:
                continue
            
            left = dic.get(num - 1, 0)
            right = dic.get(num + 1, 0)
            length = left + 1 + right

            dic[num] = length
            if left:
                dic[num - left] = length
            
            if right:
                dic[num + right] = length
            
            ans = max(ans, length)
        return ans
        