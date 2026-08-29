# Pattern: Binary Search on Answer
# Idea: search capacity [max(w), sum(w)], check days needed
# Time: O(n log sum), Space: O(1)
class Solution(object):
    def shipWithinDays(self, weights, days):
        l=max(weights)
        h=sum(weights)
        def check(mid):
            current_weight=0
            daysn=1
            for w in weights:
                if current_weight+w>mid:
                    daysn+=1
                    current_weight=w
                else:
                    current_weight+=w
            return daysn<=days
            
        while l<h:
            mid=(l+h)//2
            if check(mid):
                h=mid
            else:
                l=mid+1
        return l
