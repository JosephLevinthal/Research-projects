nota = float(input("digite sua nota: "))
mensagem = input("vai receber bonificacao S/N: ")

acrescimo = nota * 0.1

if (mensagem.upper() == "S" ) :
	nota1 = acrescimo + nota
	print(nota1)
else :
	print(nota)