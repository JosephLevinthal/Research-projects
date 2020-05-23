n1 = int(input("digite o primeiro numero: "))
n2 = int(input("digite o segundo numero: "))
i = 0
j = 0
soma1 = 0
soma2 = 0
while(i<n1):
	if(i != 0):
		if(n1 % i == 0):	
			soma1 = soma1 + i
	i = i + 1
print(soma1)

while(j<n2):
	if(j != 0):
		if(n2% j == 0):	
			soma2 = soma2 + j
	j = j + 1
print(soma2)

if(soma1 == n2 and soma2 == n1):
	print("AMIGOS")
else:
	print("NAO AMIGOS")

