nota=float(input("digite a nota"))
mensagem=input("mensagem")
acrescimo=10/100*nota
if (mensagem.upper()=="S"):
	resposta=nota+acrescimo
else:
	resposta=nota
print(resposta)