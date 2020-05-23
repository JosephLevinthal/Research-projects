x = float(input("bote a nota ai")) #mema coisa, basta olhar pra saída ou pensar que as notas no colegios tem decimais. 
opcao = input("S/N")
if (opcao.upper()) == "S":
	x = x + x*0.10
else:
	x = x
print (x)