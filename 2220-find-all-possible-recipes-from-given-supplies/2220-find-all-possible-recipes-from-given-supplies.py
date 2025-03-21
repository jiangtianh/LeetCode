class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies)
        graph = collections.defaultdict(list)
        n = len(recipes)
        visited = set()
        canMake = set(supplies)

        for i in range(n):
            recipe = recipes[i]
            graph[recipe] = []
            for ingredient in ingredients[i]:
                graph[recipe].append(ingredient)
        
        def f(recipe):
            if recipe in supplies:
                return True
            elif recipe not in graph or recipe in visited:
                return False
            visited.add(recipe)
            for ingredient in graph[recipe]:
                if not f(ingredient):
                    return False

            supplies.add(recipe)
            return True


        res = []
        for recipe in recipes:
            if f(recipe):
                res.append(recipe)
        return res