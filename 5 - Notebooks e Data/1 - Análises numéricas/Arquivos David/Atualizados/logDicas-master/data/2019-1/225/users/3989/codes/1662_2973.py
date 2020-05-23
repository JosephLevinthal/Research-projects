So = int(input("Digite posicao inicial:"))
v = int(input("Digite velocidade do objeto:"))
t = int(input("Digite tempo de deslocamento:"))


S = So + v*t
print(round(S,1))
if (v<=100):
	print("OK")
else:
	print("ACIMA")
