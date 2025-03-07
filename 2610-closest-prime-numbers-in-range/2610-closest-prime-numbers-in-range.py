class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def is_prime(num):
            if num == 1:
                return False # 1 isn't prime
            for divisor in range(2, int(sqrt(num)) + 1): # only need to check nums up to square root
                if num % divisor == 0:
                    return False # found divisible num, not prime
            return True # num wasn't divisible so prime

        pair = [] # pair w/ lowest difference
        prev = None # [prev, num] is current pair
        for num in range(left, right + 1):
            if not is_prime(num): continue # skip if not a prime number

            if not prev:
                prev = num # first prime found, can't form pair
                continue

            dif = num - prev # get difference in pair

            if dif <= 2: 
                return [prev, num] # found smallest possible difference

            if not pair or dif < pair[1] - pair[0]:
                pair = [prev, num] # found new lowest difference

            prev = num # update for new current pair [num, next prime found]

        return pair or [-1, -1] # return found pair or [-1, -1] if no pair found