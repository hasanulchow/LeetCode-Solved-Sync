class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        for row in box:
            i = 0   # Pointer to the boundary between the stone and the empty space in the current row
            for j, ch in enumerate(row):
                if ch == '*':
                    i = j+1     # Skip the obstacle
                elif ch == '.': 
                    row[i], row[j] = row[j], row[i]     # Swap empty plase and stone
                    i += 1      
        # Rotate the box clockwise
        return [col for col in zip(*reversed(box))]