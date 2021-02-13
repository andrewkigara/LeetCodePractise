class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum = 0;

        for i in nums:
            int(i)
            for x in nums:
                int(x)

#               Checks if the index is the same, it can't be the same
                if nums.index(i)==nums.index(x):
                    n=0
                else:
#               Continues if the index is different
                    sum = x+i
                    if sum == target:
                        return nums.index(i), nums.index(x)
                    else:
                        sum = 0
