camp = input("digite o resultado: ")
camp = camp.lower
t = 0
v = 0
soma = 0
while(camp != "x"):
	if(camp == "v" or "e" or "d"):
		if(camp == "v"):
			v = 3
		if(camp == "e"):
			v = 2
		if(camp == "d"):
			v = 1
		t = t + 3
	else:
		t = t + 0
	soma = soma + v
	print(t)
	print(soma)
total = (soma/t)*100
print(round(total,2))