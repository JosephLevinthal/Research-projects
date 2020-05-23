from numpy import*
p = array(eval(input("digite o peso: ")))
h = array(eval(input("digite a altura: ")))
a = 0


for i in range(size(h)): 	
	a = a + 1
	
c = zeros(a, dtype=float)
for i in range(size(h)):
		c[i] = round(c[i]+p[i]/(h[i]**2), 2)
		


if max(c)<17:
	r = "MUITO ABAIXO DO PESO"
elif max(c)>+17 and max(c)<=18.49:
	r = "ABAIXO DO PESO "
elif max(c)>=18.50 and max(c)<= 24.99:
	r = "PESO NORMAL"
elif max(c)>=24 and max(c)<=29.99:
	r = "ACIMA DO PESO"
elif max(c)>= 30 and max(c)<= 34.99:
	r = "OBESIDADE"
elif max(c)<= 35 and max(c)<=39.99:
	r = "OBESIDADE SEVERA"
elif max(c)>=40:
	r = "OBESIDADE MORBIDA"
	
print(c)

print("O MAIOR IMC DA TURMA EH:",max(c))

print(r)


	

