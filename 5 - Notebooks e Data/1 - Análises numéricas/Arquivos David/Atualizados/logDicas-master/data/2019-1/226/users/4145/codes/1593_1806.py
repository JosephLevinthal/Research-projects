from math import*

nump = int(input("numero de pessoas")) 
p = 1 - (factorial(365) / factorial(365 - nump)) * (1 / 365**nump) 
prob = p*100
print(round(prob,2))