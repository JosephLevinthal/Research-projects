from numpy import*
ast=int(input("Numero de asteristicos: "))#Número de asteristicos
v=0#Acumuladora
a='*'#Asteristico
for i in range(ast):# Primeira parte
		w=ast+v
		v-=1
		print(w*a)
a='*'#Asteristico
v=0#Acumuladora
for i in range(ast):# Segunda parte
	v+=1
	print(v*a)