class Solution(object):
    def maxArea(self, height):
        l,r=0,len(height)-1
        max_water=0
        while l<r:
            width=r-l 
            area=min(height[l], height [r])*width
            max_water=max(area,max_water)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return max_water 
