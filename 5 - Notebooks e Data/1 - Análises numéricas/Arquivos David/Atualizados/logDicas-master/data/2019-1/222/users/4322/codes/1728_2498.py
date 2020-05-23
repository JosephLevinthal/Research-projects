a = int(input("habitantes de A: "))
b = int(input("habitantes de B: "))
percentual_de_a = float(input("porcentagem da cidade A: "))
percentual_de_b = float(input("porcentagem da cidade B: "))
ab = a - b
aa = 0
ba = 0
cont = 0
while(a < b):
	hab_a = a * (percentual_de_a / 100)
	a = a + hab_a
	
	hab_b = b * (percentual_de_b / 100)
	b = b + hab_b
	cont = cont + 1
print(cont)