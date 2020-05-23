n=int(input("numero de pessoas:"))
from math import *
pr=(1-((factorial(365)/factorial(365-n))*(1/365**n)))
a=pr*100
print(round(a,2))