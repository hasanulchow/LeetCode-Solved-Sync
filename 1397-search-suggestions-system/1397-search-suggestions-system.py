import bisect

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # Sort the list of products lexicographically.
        products.sort()
        
        # Initialize the result list and an empty string 'cur' to build the search prefix.
        res, cur = [], ''
        
        # Loop through each character in the search word.
        for c in searchWord:
            # Add the current character to the prefix 'cur'.
            cur += c
            
            # Use bisect_left to find the first position where 'cur' could be inserted
            # to maintain sorted order (i.e., the first word that is >= 'cur').
            i = bisect.bisect_left(products, cur)
            
            # Filter the products starting from index 'i', and include only those that start with 'cur'.
            # We take up to 3 products starting from index 'i' and that start with the current prefix.
            res.append([w for w in products[i:i+3] if w.startswith(cur)])
        
        # Return the result containing lists of suggestions for each prefix of the searchWord.
        return res
