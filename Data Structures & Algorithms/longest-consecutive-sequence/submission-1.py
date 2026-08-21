class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = {}
        maxi = 0

        for i in nums:
            if i in dic:
                continue

            left = dic.get(i - 1, 0)
            right = dic.get(i + 1, 0)

            length = left + 1 + right

            # Current number
            dic[i] = length

            # Update left boundary
            if left:
                dic[i - left] = length

            # Update right boundary
            if right:
                dic[i + right] = length

            maxi = max(maxi, length)

        return maxi