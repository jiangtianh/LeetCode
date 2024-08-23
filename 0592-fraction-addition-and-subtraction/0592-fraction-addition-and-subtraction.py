class Solution:
    def fractionAddition(self, expression: str) -> str:
        numerators = []
        denominators = []
        symbol = []
        
        i = 0
        if expression[0] == "-":
            symbol.append("-")
            i += 1
        else:
            symbol.append("+")
        
        while i < len(expression):    
            numerator = ""
            while expression[i] != "/":
                numerator += expression[i]
                i += 1
            i += 1
            denominator = ""
            while i < len(expression) and expression[i].isnumeric():
                denominator += expression[i]
                i += 1
            numerators.append(int(numerator))
            denominators.append(int(denominator))

            if i < len(expression):
                symbol.append(expression[i])
                i += 1
        def simplify(x, y):
            gcd = math.gcd(x, y)
            return x // gcd, y // gcd

        n = len(numerators)
        numerator = 0
        denominator = 1
        for i in range(n):
            nu, de, sym = numerators[i], denominators[i], symbol[i]
            newNumerator = numerator
            newDenominator = denominator
            if de != denominator: 
                newNumerator *= de
                newDenominator *= de
                nu *= denominator

            if sym == "+":
                newNumerator += nu
            else:
                newNumerator -= nu
            
            numerator, denominator = simplify(newNumerator, newDenominator)
        

        return str(numerator) + "/" + str(denominator)