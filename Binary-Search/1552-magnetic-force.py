class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        l=1
        r=position[-1]-position[0]
        ans=0
        def can(x):
            count,last=1,position[0]
            for p in position:
                if p-last>=x:
                    count+=1
                    last =p
            if count>=m:
                return True 
            return False
                
        while l<=r:
            mid=(l+r)//2
            if can(mid):
                ans=mid
                l=mid+1
            else:
                r=mid-1
        return ans
