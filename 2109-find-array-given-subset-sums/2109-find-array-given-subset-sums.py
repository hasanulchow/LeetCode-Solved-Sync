class Solution:
    def recoverArray(self, n: int, sums: List[int]) -> List[int]:
        sums.sort()
        ans = []
        while len(sums) > 1:
            ele, sums = self._recoverArray(sums)
            ans.append(ele)
        return ans

    def _recoverArray(self, sums: List[int]) -> [int, List]:
        max_val = max(sums)
        L = len(sums)
        sums_map = {}
        for val in sums:
            if val not in sums_map:
                sums_map[val] = 0
            sums_map[val] += 1
        sorted_vals = sorted(sums_map.keys())
        init_low = sorted_vals[0]
        sums_map[init_low] -= 1
        if sums_map[init_low] == 0:
            del sums_map[init_low]
            sorted_vals.pop(0)
        for high in sorted_vals:
            _sums_map = sums_map.copy()
            _sums_map[high] -= 1
            if _sums_map[high] == 0:
                del _sums_map[high]
            count = 2
            diff = high - init_low
            ans = [init_low]
            for low in sorted_vals:
                skip_all_the_way = False
                while low in _sums_map:
                    _sums_map[low] -= 1
                    if _sums_map[low] == 0:
                        del _sums_map[low]
                    high = low + diff
                    if high not in _sums_map:
                        skip_all_the_way = True
                        break
                    _sums_map[high] -= 1
                    if _sums_map[high] == 0:
                        del _sums_map[high]
                    count += 2
                    ans.append(low)
                    if count == L:
                        skip_all_the_way = True
                        break
                if skip_all_the_way:
                    break
            if count == L:
                if 0 in set(ans):
                    return [diff, ans]
                return [-diff, [num + diff for num in ans]]