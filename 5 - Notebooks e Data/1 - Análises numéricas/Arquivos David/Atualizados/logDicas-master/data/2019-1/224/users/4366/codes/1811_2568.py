from numpy import*
v= int(input("Digite um n: "))
for i in range(v):
	print("*" * (v-i) + "o" * i + "o" * i +"*" *(v-i))


