n = int(input(" Digite o numero de pessoas em um grupo: "))
from math import factorial
x = (1 - factorial (365) / factorial(365 - n)  * (1 / 365 ** n)) * 100
print(round(x, 2))