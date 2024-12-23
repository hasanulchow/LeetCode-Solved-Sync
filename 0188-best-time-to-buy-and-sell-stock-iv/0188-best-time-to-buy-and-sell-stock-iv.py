class DoubleLinkListNode:
    # Define a node for a doubly linked list, where each node contains an index (ind),
    # a pointer to the previous node (pre), and a pointer to the next node (next).
    def __init__(self, ind, pre = None, next = None):
        self.ind = ind  # Store the index
        self.pre = pre if pre else self  # Set the previous pointer, defaulting to self (circular linked list)
        self.next = next if next else self  # Set the next pointer, defaulting to self (circular linked list)

class Solution:
    def MinMaxList(self, arr: List[int]) -> List[int]:
        # This function processes a list of numbers and returns a new list with alternating high and low values.
        n = len(arr)
        if n == 0:
            return []  # Return empty list if the input list is empty.
        
        sign = -1  # Set an alternating sign, starting with negative for comparisons.
        res = [9999]  # Initialize a result list with a placeholder value.
        
        for num in arr:
            # Alternate between high and low numbers, by comparing with the last value in res.
            if num * sign > res[-1] * sign:
                res[-1] = num  # Update last element to maintain alternating pattern.
            else:
                res.append(num)  # Add the new number if it doesn't violate the alternating pattern.
                sign *= -1  # Flip the sign to alternate between high and low values.

        # If the list length is odd, remove the last value to maintain the alternating pattern.
        if len(res) & 1:
            res.pop()

        return res  # Return the processed list.

    def maxProfit(self, k: int, prices: List[int]) -> int:
        # This function calculates the maximum profit that can be made with at most k transactions.
        newP = self.MinMaxList(prices)  # Get the MinMaxList (alternating high and low prices).
        n = len(newP)
        m = n // 2  # Half of the list length, as we process pairs of high-low.
        res = 0  # Initialize result to store profit.

        # Loop over each pair of high-low prices and calculate the profit for each pair.
        for i in range(m):
            res += newP[i * 2 + 1] - newP[i * 2]  # Add profit from each pair of high and low values.

        # If the number of profitable pairs is less than or equal to k, simply return the accumulated profit.
        if m <= k:
            return res
        
        # Create a circular doubly linked list to keep track of the nodes.
        head, tail = DoubleLinkListNode(-1), DoubleLinkListNode(-1)
        NodeList = [DoubleLinkListNode(0, head)]  # Initialize list with the first node connected to head.

        # Set up the linked list with nodes for all indices in the newP list.
        for i in range(1, n):
            NodeList.append(DoubleLinkListNode(i, NodeList[-1]))  # Append new nodes to NodeList.
            NodeList[i - 1].next = NodeList[i]  # Update the 'next' pointer of the previous node.
        
        NodeList[n - 1].next = tail  # Connect the last node to the tail.
        head.next, tail.pre = NodeList[0], NodeList[n - 1]  # Connect head to the first node, and tail to the last node.

        heap = []  # Min-heap for efficient processing of the largest profit loss.
        
        # Push all the possible pairwise profits or losses into the heap.
        for i in range(n - 1):
            if i & 1:  # If index is odd, store the loss (i.e., price difference where newP[i] > newP[i + 1]).
                heappush(heap, [newP[i] - newP[i + 1], i, i + 1, 0])
            else:  # Otherwise, store the profit (i.e., price difference where newP[i + 1] > newP[i]).
                heappush(heap, [newP[i + 1] - newP[i], i, i + 1, 1])

        # While the number of profitable pairs is greater than k, adjust the result by removing the highest loss.
        while m > k:
            loss, i, j, t = heappop(heap)  # Get the highest loss (smallest profit or largest negative value).
            if NodeList[i] == None or NodeList[j] == None: 
                continue  # Skip if either of the nodes is already deleted.
            
            m -= 1  # Decrease the number of remaining profitable pairs.
            res -= loss  # Subtract the loss from the total result.
            
            # Reorganize the linked list by removing the nodes for this pair and adjusting the links.
            nodei, nodej = NodeList[i], NodeList[j]
            nodel, noder = nodei.pre, nodej.next
            l, r = nodel.ind, noder.ind  # Get the indices of the left and right nodes.
            valL, valR = newP[l], newP[r]  # Get the values corresponding to those indices.
            noder.pre, nodel.next = nodel, noder  # Fix the links between adjacent nodes.
            NodeList[i], NodeList[j] = None, None  # Mark the nodes as deleted.

            # Depending on whether we removed a profit or loss pair, push the new pair into the heap.
            if t == 0:
                heappush(heap, [valR - valL, l, r, 1])  # Push a new profit pair.
            elif l != -1 and r != -1:
                heappush(heap, [valL - valR, l, r, 0])  # Push a new loss pair.

        return res  # Return the final accumulated profit after adjusting for at most k transactions.
