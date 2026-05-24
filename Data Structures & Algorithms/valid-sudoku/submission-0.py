class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squaresBucket = [[0]*10 for _ in range(9)]
        rowsBucket = [[0]*10 for _ in range(9)]
        colsBucket = [[0]*10 for _ in range(9)]

        for i in range(len(board)):
            for k, sN in enumerate(board[i]):
                if sN == ".":
                    continue
                
                n = int(sN)
                square = Solution.getSquareFromCoord(k, i)
                squaresBucket[square][n] += 1
                rowsBucket[i][n] += 1
                colsBucket[k][n] += 1

                dupli = squaresBucket[square][n]>1 or rowsBucket[i][n]>1 or colsBucket[k][n]>1
                if dupli == True:
                    return False

        print(squaresBucket)

        return True

    
    @staticmethod
    def getSquareFromCoord(x: int, y: int) -> int:
        return x//3 + y//3*3

