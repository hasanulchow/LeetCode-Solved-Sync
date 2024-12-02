class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        
        # Iterate until all the bits in a, b, and c are processed
        while a > 0 or b > 0 or c > 0:
            # Get the last bit of a, b, and c (using bitwise AND with 1)
            bit_a = a & 1
            bit_b = b & 1
            bit_c = c & 1

            # If the bit in c is 0, we need to flip bits in a or b (or both)
            if bit_c == 0:
                # Count how many 1's are in bit_a or bit_b because both need to be flipped to 0
                flips += (bit_a + bit_b)
            else:
                # If bit_c is 1, but both bit_a and bit_b are 0, we need to flip one of them to 1
                if bit_a == 0 and bit_b == 0:
                    flips += 1

            # Right shift a, b, and c to move to the next bit
            a >>= 1
            b >>= 1
            c >>= 1

        return flips
