class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m, n, columnIndex = len(rowSum), len(colSum), 0
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            while rowSum[i] > 0:
                minValue = min(rowSum[i], colSum[columnIndex])
                res[i][columnIndex] += minValue
                rowSum[i] -= minValue
                colSum[columnIndex] -= minValue
                if colSum[columnIndex] == 0:
                    columnIndex += 1

        return res
        