s = int(input("senha:"))
a1 = s // 100000
a2 = (s%100000)// 10000
a3 = (s% 10000) // 1000
a4 = (s % 1000) // 100
a5 = (s % 100) // 10
a6 = s% 10
x = (a2 + a4 + a6) % (a1 + a3 + a5)

if(x!= 0 ):
	msg =  "senha invalida"
else:
	msg ="acesso liberado"
print(msg)
