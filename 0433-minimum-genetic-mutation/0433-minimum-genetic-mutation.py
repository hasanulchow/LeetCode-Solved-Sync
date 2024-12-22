class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        """
        Find the minimum number of mutations required to convert the startGene to the endGene.
        Each mutation changes one character in the gene string, and the resulting gene must be in the given bank.
        :param startGene: str - The initial gene string.
        :param endGene: str - The target gene string.
        :param bank: List[str] - The set of valid gene mutations.
        :return: int - The minimum number of mutations, or -1 if it's impossible.
        """
        # Convert the bank list to a set for faster lookup
        bankSet = set(bank)
        
        # If the endGene is not in the bank, it's impossible to reach the target
        if endGene not in bankSet:
            return -1
        
        # Initialize a queue for BFS and start with the startGene
        queue = deque([startGene])
        
        # Variable to keep track of the number of mutations (steps)
        mutations = 0
        
        # Perform BFS
        while queue:
            # Process all genes at the current mutation level (level-order traversal)
            for _ in range(len(queue)):
                gene = queue.popleft()  # Get the current gene from the queue
                
                # If we've reached the target gene, return the number of mutations (steps)
                if gene == endGene:
                    return mutations
                
                # Try mutating each character of the gene
                for i in range(len(gene)):
                    # Try all possible mutations (changing the character to A, C, G, or T)
                    for c in "ACGT":
                        mutated = gene[:i] + c + gene[i+1:]  # Create the mutated gene
                        
                        # If the mutated gene is valid (exists in the bank), add it to the queue
                        if mutated in bankSet:
                            queue.append(mutated)  # Add to the queue to explore this mutation next
                            bankSet.remove(mutated)  # Remove from the bank to avoid revisiting
        
            # Increment the number of mutations (steps) after processing the current level
            mutations += 1
        
        # If no path was found, return -1
        return -1
