from math import * 
x=int(input("Digite o numero de pessoas :"))
p=1-(factorial(365)/factorial(365-x))*(1/(365**x))
p=p*100
print(round(p,2))