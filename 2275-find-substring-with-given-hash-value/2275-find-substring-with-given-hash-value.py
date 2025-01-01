class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        
        n = len(s)

        # lambda for finding the value of a character
        val = lambda v: ord(v) - ord("a") + 1

        # preprocess the powers w/ modulo to prevent overflow
        powers = [pow(power, i, modulo) for i in range(k)]
        
        # initalize our index for our substring and hash value
        idx = n-k
        hash_val = 0

        # preprocess the hash value from the n-k to n-1
        for i in range(k):
            hash_val += val(s[n-k+i]) * powers[i]

        for i in range(n-k-1, -1, -1):
            # the rolling hash part
            # update the hash value by subtracting the hash with the rightmost value times the highest power
            # then add the value of the incoming character * p1 to ensure the hash value gets updated
            hash_val = ((hash_val - val(s[i+k]) * powers[k-1]) * power + val(s[i])) % modulo
                        # removing last char in window         # adding incoming char

            # since we're reversing, the last visited instance of this if statement will be the first instance
            if hash_val == hashValue:
                idx = i
        
        return s[idx:idx+k]