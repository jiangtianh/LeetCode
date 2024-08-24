class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = []
        for i in range(query_row+1):
            tower.append([0] * (i+1))
        
        tower[0][0] = poured

        for i in range(query_row):
            for j in range(len(tower[i])):
                if tower[i][j] > 1:

                    champagnLeft = tower[i][j] - 1.0
                    tower[i][j] = 1.0

                    flowNext = champagnLeft / 2.0

                    
                    tower[i+1][j] += flowNext
                    tower[i+1][j+1] += flowNext
        return min(1, tower[query_row][query_glass])