class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        N = len(grid)
        total = N*N

        sums = sum(val for row in grid for val in row)
        sqrSum = sum(val*val for row in grid for val in row)

        perfectSum = (total * (total + 1)) // 2
        perfectSqrSum = (total * (total + 1) * (2 * total + 1)) // 6

        sumDiff = sums - perfectSum
        sqrDiff = sqrSum - perfectSqrSum

        x = (((sqrDiff // sumDiff) + sumDiff) // 2)
        y = (((sqrDiff // sumDiff) - sumDiff) // 2)

        return [x,y]


        