class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [[enqueueTime, i, processingTime] for i, (enqueueTime, processingTime) in enumerate(tasks)]
        
        res = []
        tasks.sort(key=lambda x: x[0])
        timer = tasks[0][0]
        waitingQueue = []
        i = 0

        while i < len(tasks) or waitingQueue:
            if not waitingQueue and i < len(tasks) and timer < tasks[i][0]:
                timer = tasks[i][0]

            while i < len(tasks) and timer >= tasks[i][0]:
                enqTime, idx, procTime = tasks[i]
                heapq.heappush(waitingQueue, (procTime, idx))
                i += 1
            
            processingTime, idx = heapq.heappop(waitingQueue)
            res.append(idx)
            timer += processingTime
        
        return res


        