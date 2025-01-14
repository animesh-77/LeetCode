class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:

        numFreq= {}

        ret= []
        match= 0

        for numA, numB in zip(A, B):
            numFreq[numA]= numFreq.get(numA, 0)+ 1
            numFreq[numB]= numFreq.get(numB, 0)+ 1

            if numA == numB:
                match += 1

            else:
                if numFreq[numA] == 2:
                    match += 1
                if numFreq[numB] == 2:
                    match += 1

            ret.append(match)
        print(ret)
        return ret
        