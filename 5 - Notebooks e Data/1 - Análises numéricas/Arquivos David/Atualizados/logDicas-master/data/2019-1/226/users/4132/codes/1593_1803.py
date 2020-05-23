from math import *

numero=int(input("Digite um numero de 4 digitos: "))

a=(numero//1000)*5
b=((numero%1000)//100)*4
c=(((numero%1000)%100)//10)*3
d=(((numero%1000)%100)%10)*2

digito = (a+b+c+d)%11
digito = abs(digito)

print(digito)
