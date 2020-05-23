nota=float(input("Qual foi a sua nota?: "))
boni=input("VAI receber bonificacao?: ")
if( boni== "S"):
	mensagem = nota + nota*0.1
else:
	mensagem = nota
print(mensagem)	