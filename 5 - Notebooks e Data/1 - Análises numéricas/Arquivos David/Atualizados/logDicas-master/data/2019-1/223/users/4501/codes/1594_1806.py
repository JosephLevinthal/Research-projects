from math import*
n=int(input("Digite um numero: "))
a=(1-(365/(365-n)*1/365**n))

print(round(a, 2))
