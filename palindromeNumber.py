class Solution:
    def isPalindrome(self, x: int) -> bool:
        originalNumber = x
        reversedNumber = 0

        # if x<1:
        #     x *= -1


        while x>=1:
            lastDigit = x%10
            reversedNumber = (reversedNumber*10)+lastDigit
            x //= 10

        # if originalNumber<1:
        #     reversedNumber *= -1

        if reversedNumber == originalNumber:
            return True
        else:
            return False
        
