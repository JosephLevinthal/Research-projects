val = float(input("valor: "))
qua = int(input("n. rurull: "))
tic = float(input("valor tic: "))
pas = int(input("quantidade de pas: "))
vdp = float(input("valor dos pas"))
soma = (qua*tic)+(pas*vdp)
if (soma<=val):
	print("suficiente".upper())
else:
	print("insuficiente".upper())
