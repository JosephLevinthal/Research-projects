so = int(input("insira a posicao inicial:"))
v = int(input("insira a velocidade:"))
t = int(input("insira o tempo:"))

S = so + (v * t)
print(S)

if(v >100):
	print("ACIMA")
else:
	print("OK") 