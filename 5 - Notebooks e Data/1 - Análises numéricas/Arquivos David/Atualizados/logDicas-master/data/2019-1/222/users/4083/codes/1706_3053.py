peso = float(input("digite o peso: "))

valor1 = peso*0.03 + 20
valor2 = peso*0.04 + 25
valor3 = peso*0.05 + 30
valor4 = peso*0.06 + 35

if  (peso > 0 and peso <= 5000):
     print(valor1)
		
elif(peso > 5000 and peso <= 6000):
	 print(valor2)
		
elif(peso > 6000  and peso <= 7000):
	 print(valor3)
		
else:
	 print(valor4)