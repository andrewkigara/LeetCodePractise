class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = []
        for i in range(len(nums)):
            if(i<0):
                runningSum.append(nums[0])
            else:
                sums=0
                while i>=0:
                    sums += int(nums[i])
                    i-=1
                runningSum.append(sums)

        return runningSum
