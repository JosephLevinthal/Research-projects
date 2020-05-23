# Ao testar sua solução, não se limite ao caso de exemplo.
m = int(input())
mes = ["janeiro","fevereiro","marco","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
if m not in range(1,13):
	print("numero de mes invalido")
else:
	print(mes[m-1])