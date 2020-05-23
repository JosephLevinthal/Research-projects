r = "k"
soma = 0
y = 0
j = 0
while(r != "X"):
	r = input("Insira o resultado: ").upper
	if(r == "V"):
		y = 3
		j = j + 1
	elif(r == "E"):
		y = 1
		j = j + 1
	elif(r == "D"):
		y = 0
		j = j + 1
	soma = soma + y
	
m = j * 3
p = (soma / j) * 1 /100
print(m)
print(p)

