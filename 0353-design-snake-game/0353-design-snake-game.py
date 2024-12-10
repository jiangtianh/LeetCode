class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.height = height
        self.width = width
        self.snake = collections.deque()
        self.snake.append((0, 0))
        self.body = set()
        self.body.add((0, 0))
        self.dirs = {"R": (0, 1), "D": (1, 0), "L": (0, -1), "U": (-1, 0)}        
        self.food = food
        self.foodIdx = 0
        self.score = 0
        


    def move(self, direction: str) -> int:
        newX, newY = self.snake[-1][0] + self.dirs[direction][0], self.snake[-1][1] + self.dirs[direction][1]

        # Remove the tail from the body temporarily for accurate collision checking
        tailX, tailY = self.snake.popleft()
        self.body.remove((tailX, tailY))

        # Check if the new head position is valid
        if not (0 <= newX < self.height and 0 <= newY < self.width and (newX, newY) not in self.body):
            return -1

        # Add the tail back if no food is eaten, as it moves
        if self.foodIdx < len(self.food) and newX == self.food[self.foodIdx][0] and newY == self.food[self.foodIdx][1]:
            self.snake.appendleft((tailX, tailY))  # Put the tail back as it grows
            self.body.add((tailX, tailY))
            self.foodIdx += 1
            self.score += 1

        # Add the new head position
        self.snake.append((newX, newY))
        self.body.add((newX, newY))

        return self.score


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)