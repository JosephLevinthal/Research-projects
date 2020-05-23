idade = int(input("idade: "))
imc = float(input("IMC: "))

 			
d = "Dados invalidos"
r1 = "Risco: Alto "  				
r2 = "Risco: Médio"
r3 = "Risco: Baixo"
				
if(idade<45 and imc < 22):
	print("Entradas:", idade, "anos","e","IMC", imc)				
	print(r3)
elif(idade>= 45 and imc <22)or (imc>=22 and idade>=45):
	print("Entradas:", idade, "anos","e","IMC", imc)				
	
	
	
	
	
	
	
	
	