from math import*
n=int(input("Numero de pessoas da sala:"))
f= (1-(factorial(365)/factorial(365-n))*1/365**n)*100
print(float(round(f,2)))
