// MoneyInLeetCodeBank.java

class Solution {
    public int totalMoney(int n) {
        int counter = 1;
        int days = 0;
        int dayIncAmount = 1;
        int weekIncAmount = 1;
        int money = 0;

        while (counter <= n){

            money += dayIncAmount;
            dayIncAmount ++;

            if(counter==7){
                weekIncAmount++;
                dayIncAmount = weekIncAmount;
                n -= 7;
                counter = 0;
            }


            // dont touch counter
            counter++;
        }
        return money;
    }
}
