class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        
        def f(worker, bike):
            return abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])
        
        li = []

        for workerNum, workerLocation in enumerate(workers):
            for bikeNum, bikeLocation in enumerate(bikes):
                li.append([f(workerLocation, bikeLocation), workerNum, bikeNum])
            
        li.sort()

        res = [-1] * len(workers)
        usedBike = set() 
        workersGotBike = set() 

        for distance, worker, bike in li:
            if worker not in workersGotBike and bike not in usedBike:
                usedBike.add(bike)
                workersGotBike.add(worker)
                res[worker] = bike
        
        return res
            

