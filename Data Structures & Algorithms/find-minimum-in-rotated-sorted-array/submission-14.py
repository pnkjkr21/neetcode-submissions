class Solution:
    def findMin(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        ans = 0

        while i < j:
            mid = i + (j - i) // 2
            if nums[mid] > nums[j]:
                i = mid + 1
            else:
                ans = mid
                j = mid
        print(ans)

        return nums[j]