a1 = float(input("Insira a sua altura: "))              #a sua altura
a2 = float(input("Insira a altura do acompanhante: "))  #a altura do seu amigo
if(a1 >= 1.37):         # mensagem
	msg = "Sim"          # mensagem
	print(msg)
else:                   # mensagem
	if(a2 >= 1.37):      # mensagem
		msg = "Sim"       # mensagem
		print(msg)
	else:                # mensagem
		msg = "Nao"       # mensagem
		print(msg)

if(a1 >= a2):            # ordem
	print(a1)            # ordem
if(a2 > a1):            # ordem
	print(a2)            # ordem