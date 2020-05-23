from math import*
x=int(input("Numero de pessoas: "))
c=1-((factorial(365))/(factorial(365-x)))*((1)/365**x)
c=c*100
print(round(c,2))