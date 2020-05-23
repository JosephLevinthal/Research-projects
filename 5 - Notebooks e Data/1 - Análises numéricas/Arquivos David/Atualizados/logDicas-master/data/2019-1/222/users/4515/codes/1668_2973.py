pinicial   =    int(input("Posicao Inicial metros :"))
velocidade =    int(input("Velocidade metros/seg  :")) 
tdeslocamento = int(input("Tempo do deslocamento segundos :"))

percurso = pinicial+(velocidade*tdeslocamento)

print(percurso)

if(velocidade > 100):
	print("ACIMA")
else:
	print("OK")
	
