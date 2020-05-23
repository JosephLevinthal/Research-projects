s=int(input("digite o numero: "))

for i in range(s):
	a= (s-i)* "*" + "o"*i + "o"*i +(s-i)*"*"
	print(a)