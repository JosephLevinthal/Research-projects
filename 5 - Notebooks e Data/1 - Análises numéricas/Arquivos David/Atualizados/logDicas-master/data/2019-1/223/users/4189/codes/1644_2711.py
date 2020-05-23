valor = int(input("v:"))
qtick = int(input("q:"))
vtick = float(input("v:"))
ponibus = int(input("q:"))
vpasses = float(input("v:"))
soma = (valor) - (qtick*vtick + ponibus*vpasses)
if(soma>=0):
	print("suficiente".upper())
else:
	print("insuficiente".upper())