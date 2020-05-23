from math import*
n=int(input("pessoas:"))

p=1-(factorial(365)/factorial(365-n))*(1/365**n)
s=p*100
print(round(s,2))