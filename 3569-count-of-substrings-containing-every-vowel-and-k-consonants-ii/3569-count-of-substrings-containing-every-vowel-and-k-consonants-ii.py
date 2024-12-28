class Solution:
    def countOfSubstrings(self, w: str, k: int) -> int:
        def solve(w, k):
            c = Counter()  # Counter to track occurrences of vowels and consonants
            j = 0  # Start of the window
            z = 0  # This will store the number of valid substrings
            
            for i in range(len(w)):  # Sliding window
                if w[i] in 'aeiou':  # If it's a vowel, count it
                    c[w[i]] += 1
                else:  # Else it's a consonant, represented by '_'
                    c['_'] += 1
                
                # Move the window if all vowels are present and we have k consonants
                while c['a'] > 0 and c['e'] > 0 and c['i'] > 0 and c['o'] > 0 and c['u'] > 0 and c['_'] >= k:
                    if w[j] in 'aeiou':  # Adjust the count of vowels when moving the window
                        c[w[j]] -= 1
                    else:
                        c['_'] -= 1  # Adjust the consonant count
                    j += 1  # Slide the window forward
                
                z += j  # Add valid substrings count
            return z
        
        # Count substrings with exactly k consonants by subtracting those with k+1 consonants
        return solve(w, k) - solve(w, k + 1)