class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        # Initialize an empty string to build the modified result
        modified = ""
        
        # 'previous' keeps track of the last index after inserting a space
        previous = 0
        
        # Iterate through the list of space indices
        for i in spaces:
            # Add the substring from 'previous' to 'i' (excluding 'i'), followed by a space
            modified += s[previous:i] + " "
            # Update 'previous' to the current index 'i'
            previous = i
        
        # After the loop, add the remaining part of the string starting from 'previous' to the end
        modified += s[previous:]
        
        # Return the modified string with spaces inserted
        return modified

        