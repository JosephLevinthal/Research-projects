nota = float(input("Nota do Respectivo aluno: "))
msg = input("Aluno recebera bonificacao? ")

eq = nota + ((10/100) * nota)
if (msg.upper() == "S"):
	rsp = eq
else: 
	rsp = nota

print(rsp)
	
	