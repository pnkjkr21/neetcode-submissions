class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i, j = 1, max(piles)
        ans = 0
        while i <= j:
            mid = i + (j - i)//2
            if self.validate(mid, piles, h):
                ans = mid
                j = mid - 1
            else:
                i = mid + 1
        return ans
    
    def validate(self, mid, piles, h):
        hours = 0
        for pile in piles:
            if pile % mid == 0:
                hours += pile // mid
            
            else:
                hours += pile // mid + 1
        return (hours <= h)

        