temp=input("Em que escala esta a temperatura: ")
v=float(input("Valor da temperatura: "))
if (temp == "F"):
	total=5/9*(v-32)
else:
	total=v*(9/5)+32
print(round(total, 2))	