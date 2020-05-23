d= int(input("insira o codigo: "))
d1=d%10
d2=d//10 %10
d3=d//100 %10
d4=d//1000%10
d5=d//10000%10
d6=d//100000%10
s1=d2+d4+d6
s2=d1+d3+d5
p1=s1%s2
p2=s2%s1
v="acesso liberado"
f="senha invalida"
if p1==0 or p2==0 :
	print(v)
else:
	print(f)
