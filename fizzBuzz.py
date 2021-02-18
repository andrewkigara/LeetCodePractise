# 40ms runtime
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        count=1
        out = []
        while count<=n:
            fb=""
            if count%3==0:
                fb+="Fizz"
            if count%5==0:
                fb+="Buzz"
            if fb:
                out.append(fb)
            else:
                out.append(str(count))
            count+=1
        return out


# 24ms runtime
# class Solution:
#     def fizzBuzz(self, n: int) -> List[str]:
#         ret=[]
#         for i in range(1,n+1):
#             # print(i)
#             if(i%3==0 and i%5==0):
#                 ret.append("FizzBuzz")
#             elif(i%3==0):
#                 ret.append("Fizz")
#             elif(i%5==0):
#                 ret.append("Buzz")
#             else:
#                 ret.append(str(i))
#         return(ret)
