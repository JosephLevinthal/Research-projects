nota = float(input())

resposta = input()

acrescimo= (nota*10) /100

final = nota + acrescimo

if(resposta == 'S'):
	mensagem = round(final,2)
elif (resposta == 'N'):
	 mensagem = round(nota,2)

print(mensagem)