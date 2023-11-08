class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        def getNewGene(old, i, c):
            return old[:i] + c + old[i+1:]

        geneBank = set(bank)
        q = collections.deque()

        changes = ['A', 'C', 'G', 'T']

        q.append(startGene)
        count = 0

        seen = set() 
        seen.add(startGene)

        while q:
            count += 1
            for _ in range(len(q)):
                cur = q.pop() 

                for i in range(len(cur)):
                    for newC in changes:
                        newGene = getNewGene(cur, i, newC)
                        if newGene in geneBank:
                            if newGene == endGene:
                                return count
                            if newGene not in seen:
                                q.append(newGene)
                                seen.add(newGene)

        return -1

