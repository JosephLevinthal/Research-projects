from math import*
e= int(input("n: "))
f= 1-((factorial(365))/(factorial(365-e)))* 1/(365**e)
print(round(f*100, 2))