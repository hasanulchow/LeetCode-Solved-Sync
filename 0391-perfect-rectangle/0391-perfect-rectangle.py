class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        # calculate the area of all the rectangles
        area = 0
        corners = set()
        for x1, y1, x2, y2 in rectangles:
            area += (x2 - x1) * (y2 - y1)
            # check if each corner is unique
            for corner in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
                if corner in corners:
                    corners.remove(corner)
                else:
                    corners.add(corner)
        # check if all corners are unique
        if len(corners) != 4:
            return False
        # calculate the area of the union rectangle
        x1, y1 = float("inf"), float("inf")
        x2, y2 = float("-inf"), float("-inf")
        for x, y in corners:
            x1 = min(x1, x)
            y1 = min(y1, y)
            x2 = max(x2, x)
            y2 = max(y2, y)
        union_area = (x2 - x1) * (y2 - y1)
        # check if the total area of all the rectangles is equal to the area of the union rectangle
        if area != union_area:
            return False
        # check if the total number of corners is equal to the sum of the areas of the rectangles divided by the area of a single rectangle
        return area == (x2 - x1) * (y2 - y1)