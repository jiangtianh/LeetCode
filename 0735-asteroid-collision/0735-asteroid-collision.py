class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:
            if ast < 0:
                app = True
                while stack and stack[-1] > 0 and ast < 0:
                    prev = stack.pop()
                    if abs(ast) == prev:
                        app = False
                        break
                    elif abs(ast) < prev:
                        ast = prev
                if app:
                    stack.append(ast)

            else:
                stack.append(ast)

        return stack