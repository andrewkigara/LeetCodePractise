import math
import timeit

def countVowelStrings(n):
    k= (math.factorial(n+5-1))
    j = math.factorial(n)*math.factorial(4)
    l=k/j
    return l

def countVowelStringsLong(n):
    return ((math.factorial(n+5-1)) / (math.factorial(n)*math.factorial(4)))


start = timeit.default_timer()
print(countVowelStrings(2))
stop = timeit.default_timer()
short_func = stop-start

start2 = timeit.default_timer()
print(countVowelStringsLong(2))
stop2 = timeit.default_timer()
long_func = stop2-start2

print("Difference is ", short_func-long_func)
