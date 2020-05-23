from numpy import *

pali = input("digite caracteres: ")
num = len(pali)
print(pali.replace(" ","").upper())
N = pali[0]
inv = pali[-1]

if(N == inv):
	print(1)
else:
	print(0)