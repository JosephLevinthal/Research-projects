from math import*
n = int(input())
prob = 1-factorial(365)/factorial(365-n)/365**n
print(round(prob*100,2))