from numpy import*

p = array(eval(input()))
a = array(eval(input()))

imc = zeros(size(p))

i = 0
while(i < size(imc)):
	imc[i] = round(p[i] / (a[i] * a[i]), 2)
	i = i + 1

print(imc)
maior = round(max(imc), 2)
print("O MAIOR IMC DA TURMA EH: " + str(maior))
if(maior < 17):
	print("MUITO ABAIXO DO PESO")
elif(maior >= 17) and (maior <= 18.49):
	print("ABAIXO DO PESO")
elif(maior >= 18.5) and (maior <= 24.99):
	print("PESO NORMAL")
elif(maior >= 25) and (maior <= 29.99):
	print("ACIMA DO PESO")
elif(maior >= 30) and (maior <= 34.99):
	print("OBESIDADE")
elif(maior >= 35) and (maior <= 39.99):
	print("OBESIDADE SEVERA")
elif(maior > 40):
	print("OBESIDADE MORBIDA")