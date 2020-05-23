from numpy import *
ve = input("Digite uma palavra ou frase sem espaco: ")

vs = ""
for ch in ve:
	if(ch == "a" or ch == "A"):
		vs = vs
	else:
		vs = vs + ch
print(vs)		