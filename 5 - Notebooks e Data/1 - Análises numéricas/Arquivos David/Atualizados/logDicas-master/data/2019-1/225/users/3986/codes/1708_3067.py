tipo_ataque=input("tipo de ataque :")
val1=int(input("valor 1 :"))
val2=int(input("lado 2 :"))
val3=int(input("lado 3 :"))
val4=int(input("valor 4 :"))
D=(val1 + val2 + val3) * val4
if(D < 6):
	print(D)
elif (6 <= D):
	print(D)
else : 
	print("Entrada invalida")