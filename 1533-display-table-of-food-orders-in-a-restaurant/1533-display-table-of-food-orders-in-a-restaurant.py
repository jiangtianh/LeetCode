class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        
        allFood = set()
        d = collections.defaultdict(dict)
        for name, table, food in orders:
            allFood.add(food)
            instance = d[table]
            if food not in instance:
                instance[food] = 1
            else:
                instance[food] += 1
        allFood = sorted([food for food in allFood])

        res = [['Table'] + allFood]
        tableNums = [int(n) for n in d.keys()]
        tableNums.sort()
        print(tableNums)
        for tableNum in tableNums:
            temp = [str(tableNum)]
            for food in allFood:
                if food in d[str(tableNum)]:
                    temp.append(str(d[str(tableNum)][food]))  
                else:
                    temp.append('0')
            res.append(temp)

        return res
