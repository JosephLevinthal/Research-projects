from math import *
from numpy import *
li = int(input("Digite o limite inferiro do intervalo: "))
ls = int(input("Digite o limite superior do intervalo: "))
intervalo = arange(li, ls+1)

for num in intervalo:
	if(num%6 == 0):
		print(num)