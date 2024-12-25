import heapq  # Importing the heapq module to use heaps

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Initialize an empty heap and a dictionary to count the frequency of each number.
        heap = []
        counter = {}
        
        # Count the frequency of each number in 'nums' and store in 'counter'.
        for n in nums:
            counter[n] = 1 + counter.get(n, 0)
        
        # Push the frequency and corresponding number into the heap.
        # Use negative frequency (-val) to simulate a max-heap using Python's min-heap.
        for key, val in counter.items():
            heapq.heappush(heap, (-val, key))
        
        # Initialize an empty list to store the result (top k frequent elements).
        res = []
        
        # Pop the top 'k' elements from the heap and append them to the result.
        while len(res) < k:
            res.append(heapq.heappop(heap)[1])  # Extract the number (second element) from the tuple
        
        # Return the list of the 'k' most frequent elements.
        return res
