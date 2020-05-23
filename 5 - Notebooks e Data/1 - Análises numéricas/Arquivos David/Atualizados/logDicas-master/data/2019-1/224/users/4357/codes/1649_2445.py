temperatura=input("digite  a temperatura em C ou F:")
valordatemp=float(input("digite o numero"))
temperatura= temperatura.upper()
if (temperatura == "C"):
	fahrenheit= (9 * valordatemp + 100) / 5
	print(round(fahrenheit,2))
else:
	celsius= (5 / 9 + (valordatemp - 32))
	print(celsius,2)