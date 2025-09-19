class Spreadsheet:

    def __init__(self, rows: int):
        self.grid = [[0] * 26 for _ in range(rows)]

    def getCord(self, cord):
        col = ord(cord[0]) - ord("A")
        return int(cord[1:]) - 1, col
        

    def setCell(self, cell: str, value: int) -> None:
        i, j = self.getCord(cell)
        self.grid[i][j] = value

    def resetCell(self, cell: str) -> None:
        i, j = self.getCord(cell)
        self.grid[i][j] = 0

    def getValue(self, formula: str) -> int:
        formula = formula[1:].split("+")
        return self.getNum(formula[0]) + self.getNum(formula[1])
        
    def getNum(self, formula: str):
        if formula.isnumeric():
            return int(formula)
        i, j = self.getCord(formula)
        return self.grid[i][j]

# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)