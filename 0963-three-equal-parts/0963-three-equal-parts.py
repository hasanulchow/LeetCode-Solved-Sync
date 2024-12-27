class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        n = len(arr)

        # part 1

        # get total_count and create prefix_sum
        total_count = 0
        prefix_sum = [0] * n
        for i in range(n):
            total_count += arr[i]
            prefix_sum[i] = total_count

        # checking if multiple of 3
        if total_count % 3 != 0:
            return [-1, -1]
        elif total_count == 0:
            return [0, n - 1]

        # binary search to get first occurrence of `val` using prefix_sum
        def bin_search(val):
            start = 0
            end = n - 1
            mid = 0

            while start <= end:
                mid = (start + end) // 2
                if prefix_sum[mid] >= val:
                    if start == end:
                        return mid
                    end = mid
                else:
                    start = mid + 1

            return mid

        
        # count of ones in each part and count of ending_zeroes
        part_count = total_count // 3
        ending_zeroes = n - 1 - bin_search(total_count)

        # value of i and j using binary_search and ending_zeroes
        i = bin_search(part_count) + ending_zeroes + 1
        j = bin_search(total_count - part_count) + ending_zeroes + 1



        # part 2

        # disregard starting zeroes in first part
        a = 0
        while a < n and arr[a] == 0:
            a += 1

        # disregard starting zeroes in second part
        b = i
        while b < n and arr[b] == 0:
            b += 1

        # disregard starting zeroes in third part
        c = j
        while c < n and arr[c] == 0:
            c += 1

        # check if indices have same order of ones and zeroes
        while c < n:
            if arr[a] == arr[b] and arr[b] == arr[c]:
                a += 1
                b += 1
                c += 1
            else:
                return [-1, -1]

        if a == i and b == j:
            return [i - 1, j]
        else:
            return [-1, -1]