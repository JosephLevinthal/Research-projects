a = int(input("senha: "))

eve = (a//100000)%10
l = (a//10000)%10
die = (a//1000)%10
j = (a//100)%10
k = (a//10)%10
v = a%10

h = (l +j +v)%(eve + die +k)
if(h==0):
	print("acesso liberado")
else:
	print("senha invalida")
