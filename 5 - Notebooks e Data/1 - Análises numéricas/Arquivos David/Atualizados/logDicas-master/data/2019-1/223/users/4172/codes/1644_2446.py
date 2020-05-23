x=int (input("numero de 6 digitos: "))

s1=x//100000
s2=(x//10000)%10
s3=(x//1000)%10
s4=(x//100)%10
s5=(x//10)%10
s6=x%10

w=(s2+s4+s6)%(s1+s3+s5)

if w==0:
	print("acesso liberado")
else:
	print("senha invalida")