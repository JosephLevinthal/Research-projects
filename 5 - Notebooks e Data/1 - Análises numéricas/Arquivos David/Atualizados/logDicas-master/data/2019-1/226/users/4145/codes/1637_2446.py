num = int(input("semha de seis digitos: "))
a =num//100000
b = (((num/10000)*10)//10)%10
c = (((num/1000)*10)//10)%10
d = (((num/100)*10)//10)%10
e = (((num//10)*10)//10)%10
f = num%10
x = b + d + f
y = a + c + e

if(x%y  == 0 ):
	print("acesso liberado")
else:	
	print("senha invalida")