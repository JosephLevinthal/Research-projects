n=int(input())
from math import*
x= (1-((factorial(365))/(factorial(365-n)))*1/(365**n))*100
print(round(x, 2))