class Solution(object):
    def twoSum(self, numbers, target):
        l=0
        r=len(numbers)-1
        while l<r:
            C_sum=numbers[l]+numbers[r]
            if C_sum==target:
                return[l+1,r+1]
            elif C_sum<target:
                l+=1
            else:
                r-=1
        return[]
