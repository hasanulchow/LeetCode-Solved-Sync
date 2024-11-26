class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # Edge case: if there are no rooms, return False
        if not rooms: return False
        
        # Start with the keys in room 0 and mark room 0 as visited ('v')
        keys = rooms[0]
        rooms[0] = 'v'
        
        # Use a stack-like approach to explore rooms starting from the keys of room 0
        while keys:
            key = keys.pop()  # Take the last key from the stack
            if rooms[key] != 'v':  # If the room hasn't been visited
                keys += rooms[key]  # Add keys from the newly visited room to the stack
                rooms[key] = 'v'  # Mark the room as visited
        
        # Check if all rooms have been visited. If any room is not visited, return False
        for room in rooms:
            if room != 'v': return False
        
        return True  # If all rooms are visited, return True

        