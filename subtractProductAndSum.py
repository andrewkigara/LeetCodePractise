class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        nDigits = list(map(int, str(n)))
        nSum = 0
        nProd = 1

        for n in range(len(nDigits)):
            nSum += int(nDigits[n])
            nProd *= int(nDigits[n])

        return (nProd - nSum)
