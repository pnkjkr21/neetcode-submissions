class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = []
        suff = []

        if len(nums) <= 1:
            return []

        for num in nums:
            if pref:
                pref.append(num * pref[-1])
            else:
                pref.append(num)
        
        for i in range(len(nums) - 1, -1, -1):
            if suff:
                suff.append(nums[i] * suff[-1])
            else:
                suff.append(nums[i])
        
        suff.reverse()
        
        ans = []
        for i in range(len(suff)):
            if i == 0:
                ans.append(suff[i+1])
            elif i == len(suff) - 1:
                ans.append(pref[i-1])
            else:
                ans.append(suff[i+1] * pref[i-1])
        
        return ans



        