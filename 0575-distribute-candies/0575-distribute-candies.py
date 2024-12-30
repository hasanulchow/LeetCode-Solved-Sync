class Solution:
    def distributeCandies(self, candyType):
        n = len(candyType) // 2 # just get the number of candies you can eat
        LEN = len(set(candyType)) # types of different candies
        return min(n, LEN) # use min() to get the max types we can get