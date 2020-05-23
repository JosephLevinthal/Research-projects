n=int(input("numero de pessoas: "))
from math import *
p=1-((factorial(365)/factorial(365-n))*(1/(365)**n))
s=p*100
print(round(s,2))