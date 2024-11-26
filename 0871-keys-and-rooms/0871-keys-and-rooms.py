class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if (not rooms): return False
        keys = rooms[0]
        rooms[0] = 'v'
        while (keys):
            key = keys.pop()
            if rooms[key] != 'v':
                keys += rooms[key]
                rooms[key] = 'v'
        for room in rooms:
            if room != 'v': return False
        return True
        