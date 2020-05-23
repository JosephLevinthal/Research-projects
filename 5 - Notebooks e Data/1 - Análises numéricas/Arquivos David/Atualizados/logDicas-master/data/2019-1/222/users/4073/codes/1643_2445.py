escala = input()

valor = float(input())

c = (5/9) * (valor - 32)

celcus = round(c,2)

f = ((9/5)*valor) + 32

fara = round(f,2)

if( escala == 'C'):
		print(fara)
elif (escala == 'F'):
		print(celcus)