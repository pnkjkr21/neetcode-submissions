class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = self.findPivot(nums)
        if pivot > 0:
            ans = self.binarySearch(nums[:pivot], target)
            if ans != -1:
                return ans
        ans = self.binarySearch(nums[pivot:], target)
        return pivot + self.binarySearch(nums[pivot:], target) if ans != -1 else ans

    def findPivot(self, nums):
        i, j = 0, len(nums) - 1
        while i < j:
            mid = i + (j - i)//2
            if nums[mid] > nums[j]:
                i = mid + 1
            else:
                j = mid
        return j
    
    def binarySearch(self, nums, target):
        i, j = 0, len(nums) - 1
        while i <= j:
            mid = i + (j - i) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                j = mid - 1
            else:
                i = mid + 1
        return -1
        