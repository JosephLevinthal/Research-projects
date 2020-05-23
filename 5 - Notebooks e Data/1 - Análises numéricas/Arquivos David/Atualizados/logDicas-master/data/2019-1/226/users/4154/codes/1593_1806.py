import math
n = int(input('qual o numero de pessoas? '))

print(round((1-(math.factorial(365)/math.factorial(365-n))*(1/365**n))*100,2))