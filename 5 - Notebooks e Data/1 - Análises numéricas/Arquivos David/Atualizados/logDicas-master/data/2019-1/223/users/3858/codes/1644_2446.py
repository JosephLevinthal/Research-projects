s = int(input())

p = (s//100000)#primeiro
s = ((s//10000)%10)#segundo
t = (((s//1000)%10)%10)#terceiro
q = ((((s//100)%10)%10)%10)
quin = (((((s//10)%10)%10)%10)%10)
s = (s%10)

c1 = p + t + quin
c2 = s + q + s

if((c1%c2) == 0):
	print("acesso liberado")
else:
	print("senha invalida")

