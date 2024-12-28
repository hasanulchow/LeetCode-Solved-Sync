class Solution:
    def findAnswer(self, parent: List[int], s: str) -> List[bool]:
        node_to_children = [[] for _ in range(len(parent))]
        for i, p in enumerate(parent):
            if p != -1:
                node_to_children[p].append(i)

        powers = [1] * len(s)
        for i in range(1, len(s)):
            powers[i] = (powers[i-1] * 127) % (10**9 + 7)
        
        def hash_fn(ch, base=127, mod=10**9 + 7):
            return ord(ch) * base % mod

        def hash_from_hashes(lens, hashes, mod=10**9 + 7):
            hash = hashes[0]
            for l, h in zip(lens[1:], hashes[1:]):
                hash = (hash * powers[l] + h) % mod
            return hash

        res = [True] * len(parent)
        def dfs(n):
            if not node_to_children[n]:
                return 1, hash_fn(s[n]), hash_fn(s[n])
            lens, hashes, hashes_rev = list(zip(*(
                [
                    dfs(c)
                    for c in node_to_children[n]
                ] + [(1, hash_fn(s[n]), hash_fn(s[n]))]
            )))
            hash = hash_from_hashes(
                lens,
                hashes,
            )
            hash_rev = hash_from_hashes(
                lens[::-1],
                hashes_rev[::-1],
            )
            res[n] = hash == hash_rev
            return sum(lens), hash, hash_rev
        dfs(0)

        return res