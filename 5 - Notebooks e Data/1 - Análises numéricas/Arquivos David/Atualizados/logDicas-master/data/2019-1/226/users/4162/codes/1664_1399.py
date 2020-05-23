qtv1= int(input("Quantidade de votos para o candidato Ambrosio: "))
qtv2= int(input("Quantidade de votos para o candidato Demelza: "))
a= (qtv1+qtv2)
x=(qtv1*100)/a
y=(qtv2*100)/a
if qtv1>qtv2:
	print("Ambrosio Rutra")
	print(round(x,2))
if qtv2>qtv1:
	print("Demelza Olecram")
	print(round(y,2))
