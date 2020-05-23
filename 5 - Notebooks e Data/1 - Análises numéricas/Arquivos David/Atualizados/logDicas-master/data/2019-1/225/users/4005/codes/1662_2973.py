p1=int(input("posicao inicial:"))
vl=int(input("velocidade:"))
t=int(input("tempo:"))
limite = 100
S= p1+(vl*t)
if(S>=100):
	print(S)
	print("ACIMA")
else:
	print("OK")