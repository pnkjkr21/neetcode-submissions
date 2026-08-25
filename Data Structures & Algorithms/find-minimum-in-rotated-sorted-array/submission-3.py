class Solution:
    def findMin(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1

        while i < j:
            mid = i + (j - i) // 2

            if nums[mid] > nums[j]:
                # Minimum is on the right
                i = mid + 1
            else:
                # Minimum is mid or on the left
                j = mid

        return nums[i]