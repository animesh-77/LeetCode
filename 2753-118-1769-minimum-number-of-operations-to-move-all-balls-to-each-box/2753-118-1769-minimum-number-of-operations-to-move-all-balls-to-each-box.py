class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        totalMoves= []
        boxesLen= len(boxes)
        for i in range(boxesLen):
            thisBoxMoves= 0

            for j in range(boxesLen):

                if i==j:
                    continue
                if boxes[j]=="1":
                    thisBoxMoves += abs(j-i)
        
            totalMoves.append(thisBoxMoves)

        return totalMoves