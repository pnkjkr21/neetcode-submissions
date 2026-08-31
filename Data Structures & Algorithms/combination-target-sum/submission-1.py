# import sys
# sys.setrecursionlimit(10**5)
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.ans = []
        self.solve(nums, [], 0, target)
        return self.ans
    
    def solve(self, nums, arr, ind, target):
        if ind >= len(nums) or sum(arr) > target:
            return
        if sum(arr) == target:
            self.ans.append(list(arr))
            return
        self.solve(nums, arr + [nums[ind]], ind, target)
        self.solve(nums, arr, ind + 1, target)
        

        