from math import *
npessoas = int(input("Numero de alunos: "))
probab = (1 - (factorial(365)/ factorial(365 - npessoas)) * (1 / 365 ** npessoas)) * 100
print(round(probab, 2))