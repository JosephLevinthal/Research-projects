num = int(input("Digite a senha "))

d1 = num // 100000 % 10
d2 = num // 10000 % 10
d3 = num // 1000 % 10
d4 = num // 100 % 10
d5 = num // 10 % 10
d6 = num // 1 % 10

p=(d2+d4+d6)
s=(d1+d3+d5)
if(p%s):
	C="senha invalida"
else:
	C="acesso liberado"
print(C)