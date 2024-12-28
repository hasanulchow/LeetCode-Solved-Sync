# iterative pow function with constant memory

class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        alphabet = 26

        def construct_A(s):
            line = [0] * alphabet
            for char, cnt in Counter(s).items():
                index = ord(char) - 97
                line[index] = cnt
            return [line]

        def construct_B(nums):
            B = [[0] * alphabet for _ in range(alphabet)]
            for i, shift in enumerate(nums):
                for j in range(shift):
                    B[i][(i + 1 + j) % alphabet] = 1
            return B
        
        A = construct_A(s)
        B = construct_B(nums)
        modulo = 1_000_000_007

        def mult(A, B):
            n = len(A)
            m = len(B[0])
            l = len(A[0])

            C = [[0] * m for _ in range(n)]
            for i in range(n):
                for j in range(m):
                    C[i][j] = sum(
                        A[i][k] * B[k][j]
                        for k in range(l)
                    ) % modulo
            
            return C
        
        # help function
        def get_one_matrix(size):
            result = [[0] * size for _ in range(size)]
            for i in range(size):
                result[i][i] = 1
            return result
        
        # instead of pow function
        def pow_constant_memory(A, n):
            if n == 1:
                return A
            
            result = get_one_matrix(alphabet)
            for i in range(alphabet):
                result[i][i] = 1
            a_square = A
            while n:
                if n % 2 == 1:
                    result = mult(result, a_square)
                n //= 2
                a_square = mult(a_square, a_square)
            return result
        
        C = mult(A, pow_constant_memory(B, t))
        return sum(
            sum(line) % modulo
            for line in C
        ) % modulo