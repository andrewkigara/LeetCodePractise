#MoneyInLeetCodeBank.py

class Solution:
    def totalMoney(self, n: int) -> int:
        counter = 1;
        days = 0;
        dayIncAmount = 1;
        weekIncAmount = 1;
        money = 0;

        while counter <= n:
            money += dayIncAmount
            dayIncAmount+=1

            if counter==7:
                weekIncAmount+=1
                dayIncAmount = weekIncAmount
                n -= 7
                counter = 0

            # doesn't change
            counter+=1
        return money
