class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        # k will be obtained after certain number of operations
        ops_needed = 0
        curr_len = 1
        while curr_len < k:
            curr_len <<= 1
            ops_needed += 1
        operations = operations[:ops_needed] # remove unnecessary extra operations

        # every operation doubles the length
        # if k is greater than half the length, its value is obtained from the first half
        # note the number of times k transitions from 1H -> 2H with operation "1"
        op1_count = 0
        half_len = curr_len // 2
        for i in range(len(operations)-1, -1, -1):
            if k - half_len > 0:
                if operations[i] == 1:
                    op1_count += 1
                k -= half_len
            half_len = half_len // 2

        return chr(op1_count % 26 + ord("a"))
                
        
            