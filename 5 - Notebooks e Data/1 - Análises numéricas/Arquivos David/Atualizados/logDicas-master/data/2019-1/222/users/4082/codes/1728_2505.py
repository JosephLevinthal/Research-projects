import math
x = eval(input())
n = int(input())

s = 0
i = 0

while i<n:
    s = ((x ** (2 * i + 1)) * ((-1) ** (i))) / (math.factorial(2 * i + 1)) + s
    i=i+1

print(round(s,10))