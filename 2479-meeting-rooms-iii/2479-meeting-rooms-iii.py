class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        rooms = [0] * n
        roomHeap = [i for i in range(n)]
        heapq.heapify(roomHeap)
        meetingHeap = []

        for start, end in meetings:

            while meetingHeap and meetingHeap[0][0] <= start:
                time, room = heapq.heappop(meetingHeap)
                heapq.heappush(roomHeap, room)

            if not roomHeap:
                time, room = heapq.heappop(meetingHeap)
                heapq.heappush(meetingHeap, (time+(end - start), room))
                rooms[room] += 1
            else:
                roomToUse = heapq.heappop(roomHeap)

                heapq.heappush(meetingHeap, (end, roomToUse))
                rooms[roomToUse] += 1
        
        return rooms.index(max(rooms))