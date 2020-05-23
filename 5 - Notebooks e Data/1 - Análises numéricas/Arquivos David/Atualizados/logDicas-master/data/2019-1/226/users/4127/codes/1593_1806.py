from math import*
n= int(input("quantas pessoas ha no grupo? "))
pn= (1-(factorial(365)/factorial(365-n))*1/(365**n))
print(round(pn*100,2))