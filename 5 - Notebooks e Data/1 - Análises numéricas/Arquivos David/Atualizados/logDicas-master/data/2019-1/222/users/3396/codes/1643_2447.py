p_1=float(input("p_1:"))
pag=float(input("pag:"))
if(p_1>pag):
	mensagem=("Falta")
	cont=(p_1-pag)
else:
	mensagem=("Troco de")
	cont=(pag-p_1)
print(mensagem,round(cont, 2))
	