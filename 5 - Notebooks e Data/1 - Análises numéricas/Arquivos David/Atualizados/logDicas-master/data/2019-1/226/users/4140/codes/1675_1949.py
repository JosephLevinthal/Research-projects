a=int(input())
b=int(input())
c=a//10
d=a%10
e=b//10
f=b%10

if(a==b):
	print("Ganhou R$ 100.000,00")
elif(c==f and d==e):
	print("Ganhou R$ 50.000,00")
elif(c==e or c==f or d==e or d==f):
	print("Ganhou R$ 1.000,00")
else:
	print("Perdeu")