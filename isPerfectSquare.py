#24 ms

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if int(num**0.5) < float(num**0.5):
            return False
        elif int(num**0.5) > float(num**0.5):
            return False
        else:
            return True

# faster runtime

# class Solution:
#     def isPerfectSquare(self, num: int) -> bool:
#         return (num**0.5).is_integer()
