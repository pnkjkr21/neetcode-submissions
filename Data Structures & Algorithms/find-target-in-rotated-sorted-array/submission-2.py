class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = self.findPivot(nums)
        if nums[pivot] <= target <= nums[-1]:
            return self.binarySearch(nums, target, pivot, len(nums) - 1)
        return self.binarySearch(nums, target, 0, pivot - 1)

    def findPivot(self, nums):
        i, j = 0, len(nums) - 1
        while i < j:
            mid = i + (j - i)//2
            if nums[mid] > nums[j]:
                i = mid + 1
            else:
                j = mid
        return j
    
    def binarySearch(self, nums, target, i, j):
        while i <= j:
            mid = i + (j - i) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                j = mid - 1
            else:
                i = mid + 1
        return -1
        