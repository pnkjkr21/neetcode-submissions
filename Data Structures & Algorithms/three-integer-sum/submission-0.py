class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        uniq = set()
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            constant = nums[i]
            while j < k:
                if nums[j] + nums[k] > -constant:
                    k -= 1
                elif nums[j] + nums[k] < -constant:
                    j += 1
                else:
                    if (nums[i], nums[j], nums[k]) not in uniq:
                        ans.append([nums[i], nums[j], nums[k]])
                        uniq.add((nums[i], nums[j], nums[k]))
                    k -= 1
        return ans