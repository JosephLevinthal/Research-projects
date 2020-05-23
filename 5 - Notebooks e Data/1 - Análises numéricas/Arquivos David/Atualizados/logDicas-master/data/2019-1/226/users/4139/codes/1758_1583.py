from numpy import*
a = input("numero: ")
i = 2
frase = ""
while(i <= len(a)):
	frase += a[i-2] + a[i-1] + a[i] + "."
	i = i + 3
print(frase)