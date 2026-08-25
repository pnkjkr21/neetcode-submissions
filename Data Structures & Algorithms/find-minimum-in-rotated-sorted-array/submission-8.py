class Solution:
    def findMin(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        ans = 0

        while i < j:
            mid = i + (j - i) // 2

            if nums[mid] > nums[j]:
                print("hello")
                # Minimum is at mid or to the left
                i = mid + 1
            else:
                # Minimum is to the right of mid
                ans = mid
                j = mid

        return nums[j]