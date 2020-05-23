nota=float(input("digite a nota do aluno:0-10"))
bonificaçao=input("S ou N")
if bonificaçao.upper()== "S":
	nota=nota+((10*nota)/100)
print(round(nota, 1))