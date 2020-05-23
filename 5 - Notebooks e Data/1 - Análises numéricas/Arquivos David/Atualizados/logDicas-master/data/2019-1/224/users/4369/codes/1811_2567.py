from numpy import*
v = array(eval(input("Digite um numero: ")))
for i in range(v, 0, -1):
	print("*" * i)
for i in range(1, v + 1, 1):
	print("*" * i)