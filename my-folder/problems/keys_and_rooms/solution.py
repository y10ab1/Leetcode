class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = [0]
        s = set([0])
        while q:
            door = q.pop()
            s.add(door)
            for k in rooms[door]:
                if k not in s:
                    q.append(k)
        return len(rooms) == len(s)