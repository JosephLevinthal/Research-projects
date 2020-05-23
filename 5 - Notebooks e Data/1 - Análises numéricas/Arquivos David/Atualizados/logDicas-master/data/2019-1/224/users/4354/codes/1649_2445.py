temperatura = input("digite a temperatura em C ou F: ")
valor_temperatura = float(input("digite o valor da temperatura: "))
temperatura = temperatura.upper()
if(temperatura == "C") :
	fahrenheit =(9 * valor_temperatura + 160) / 5
	print(round(fahrenheit,2))
if(temperatura == "F") :
	celcius = 5/9 * (valor_temperatura - 32) 
	print(round(celcius,2))