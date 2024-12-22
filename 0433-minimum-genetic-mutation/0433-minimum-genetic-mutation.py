class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bankSet = set(bank)
        if endGene not in bankSet:
            return -1
        
        queue = deque([startGene])
        mutations = 0
        
        while queue:
            for _ in range(len(queue)):
                gene = queue.popleft()
                if gene == endGene:
                    return mutations
                
                for i in range(len(gene)):
                    for c in "ACGT":
                        mutated = gene[:i] + c + gene[i+1:]
                        if mutated in bankSet:
                            queue.append(mutated)
                            bankSet.remove(mutated)
            
            mutations += 1
        
        return -1