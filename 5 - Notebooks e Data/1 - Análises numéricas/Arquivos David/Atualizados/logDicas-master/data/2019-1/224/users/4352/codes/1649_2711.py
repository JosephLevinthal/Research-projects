# dinheiro total
v_disp = int(input("digite seu saldo: "))
# para o RU
quant_ru = int(input("digite quantos tickets de ru ce quer: "))
# valor dos tickets do RU
v_ru = float(input("digite o valor do ticket do ru: "))
# para os passes de onibus
quant_p = int(input("digite quantos passes ce quer: "))
# valor dos passes
v_p = float(input("digite o valor do passe: "))
#################################
if v_disp > (quant_ru * v_ru) + (quant_p * v_p):
	print("SUFICIENTE")
else:
	print("INSUFICIENTE")