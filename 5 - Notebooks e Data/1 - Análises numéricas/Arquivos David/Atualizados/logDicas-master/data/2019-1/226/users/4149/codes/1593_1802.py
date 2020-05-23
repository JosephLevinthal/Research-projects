from math import *
vida=int(input("digite a vida inicial: "))
dado1=int(input("digite o valor dado1: "))
dado2=int(input("digite o valor dado2: "))
golpe=int(abs(sqrt(5*dado1)+pi**(dado2/3)))
result=vida-golpe
print(result)