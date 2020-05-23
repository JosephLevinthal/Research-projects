s = int(input("digite a senha: "))

a = int(s%10)							#6º
b = int((s%100)//10)					#5º
c = int((s%1000)//100)				#4º
d = int((s%10000)//1000)			#3º
e = int((s%100000)//10000)			#2º
f = int(s/100000)						#1º

x = (e + c + a)
y = (b + d + f)
w = x%y

if w == 0:
	print("acesso liberado")

else:
	print("senha invalida")