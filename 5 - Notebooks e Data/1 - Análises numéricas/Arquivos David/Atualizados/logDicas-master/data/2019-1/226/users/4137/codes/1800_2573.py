from numpy import*

p = array(eval(input("Peso: ")))
h =  array(eval(input("Altura: ")))

im = zeros(size(p), dtype=float)

for x in range(size(p)):
	im[x] = round(p[x]/(h[x]**2), 2)
print(im)
print("O MAIOR IMC DA TURMA EH:",max(im))

s = max(im)
if (s < 17):
	print("MUITO ABAIXO DO PESO")
elif(s >= 17 and s < 18.5):
	print("ABAIXO DO PESO")
elif(s >=18.5 and s < 25):
	print("PESO NORMAL")
elif(s >= 25 and s < 30):
	print('ACIMA DO PESO')
elif(s >= 30 and s < 35):
	print("OBESIDADE")
elif(s >= 35 and s < 40 ):
	print("OBESIDADE SEVERA")
elif(s >= 40):
	print("OBESIDADE MORBIDA")