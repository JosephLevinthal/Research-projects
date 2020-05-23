acai_g = int(input())
salgado = int(input())
valor_pago = float(input())

acai_kg = acai_g / 1000.0

valor_a_pagar = (acai_kg * 24.0) + (salgado * 3.0)

print(round(valor_a_pagar, 2))

if(valor_pago > valor_a_pagar):
	print("Sim")
else:
	print("Nao")