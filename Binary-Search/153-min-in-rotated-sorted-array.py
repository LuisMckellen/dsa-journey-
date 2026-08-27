class Solution(object):
    def findMin(self, nums):
        l=0
        h=len(nums)-1
        while l<h:
            mid=(l+h)//2
            if nums[mid]>nums[h]:
                l=mid+1
            else:
                h=mid
        return nums[l]
