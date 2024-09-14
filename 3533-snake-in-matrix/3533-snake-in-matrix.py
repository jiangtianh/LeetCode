class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        cur = 0

        for command in commands:
            if command == "RIGHT":
                cur += 1
            elif command == "LEFT":
                cur -= 1
            elif command == "DOWN":
                cur += n
            else:
                cur -= n
        return cur