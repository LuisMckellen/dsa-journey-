class Solution(object):
    def splitArray(self, nums, k):
        l=max(nums)
        h=sum(nums)
        def check(mid):
            c_sum=0
            count=1
            for i in nums:
                if c_sum+i>mid:
                    count+=1
                    c_sum=i
                else:
                    c_sum+=i
            return count<=k
            
        while l<h:
            mid=(l+h)//2
            if check(mid):
                h=mid
            else:
                l=mid+1     
        return l
