s = int(input("insira senha: "))

a = s//100000
b = s//10000%10
c= s//1000%10
d = s//100%10
e = s//10%10
f= s % 10

x = (b+d+f)
y =(a+c+e)

if (x%y==0):
	msg =("acesso liberado")
else:
	msg =("senha invalida")

print(msg)