gramas = float(input("g: "))
num_bebidas = int(input("bebidas: "))
quant_sobremesas = int(input("sobremesas: "))
pf = (gramas * 26.90) / 1000
sn = 3.50 * num_bebidas
sobremesa = 3.0 * quant_sobremesas
preco_a_ser_pago = pf + sn + sobremesa
print(round(preco_a_ser_pago, 2))