class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.snake = collections.deque([(0, 0)])
        self.body = {(0, 0)}
        self.food = collections.deque(food)
        self.m = width
        self.n = height
        self.dirs = {"R": [0, 1], "L": [0, -1], "D": [1, 0], "U": [-1, 0]}

    def check(self, position):
        x, y = position
        return 0 <= x < self.n and 0 <= y < self.m and (x, y) not in self.body

    def move(self, direction: str) -> int:
        i, j = self.dirs[direction]
        newPosition = (self.snake[-1][0] + i, self.snake[-1][1] + j)

        scored = self.food and newPosition[0] == self.food[0][0] and newPosition[1] == self.food[0][1]

        if not scored:
            tailPosition = self.snake.popleft()
            self.body.remove(tailPosition)
         
        if not self.check(newPosition):
            return -1

        self.snake.append(newPosition)
        self.body.add(newPosition)
        

        if scored:
            self.food.popleft()

        return len(self.body) - 1
        



# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)