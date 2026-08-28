class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        res=r
        while l<=r:
            total=0
            k=(l+r)//2
            for i in piles:
                total+=(i+k-1)//k
            if total<=h:
                res=k
                r=k-1
            else:
                l=k+1
        return res
