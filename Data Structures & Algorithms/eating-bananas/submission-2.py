import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # realistically, eating speed should be consistent with one of the piles
        # we want to minimize, array isnt sorted
        # h is always greater or equal to len of piles. 
        # max eating speed, or upper bound is max of the banana piles 

        # itll take ceil(x/k) time to finish x pile with rate of k banana an hour

        r = 0

        for pile in piles: # O(n)
            r = max(r, pile)

        # now we search for the minimum that satisfies hours under h
        l = 1

        while l < r:
            mid = (r + l)//2

            # see if this satisfies 
            hours_needed = sum(math.ceil(pile / mid) for pile in piles)
            
            # if it doesnt work, we have to try the lower half
            if hours_needed > h:
                l = mid + 1

            # if it works, try another smaller one?
            elif hours_needed <= h:
                r = mid

        return l

