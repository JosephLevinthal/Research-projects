num = int(input("Numero: "))

str = "*"

for p in range(num, 0, -1): #Invertendo a função range, começando do maior para o menor com ordem "-1"
	print(str*p)	
for i in range(num+1):
	print(str*i)