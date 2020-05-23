p = array(eval(input("Pesos: ")), dtype=float)
a = array(eval(input("Alturas: ")), dtype=float)
s = size(p)
z = zeros(s, dtype=float)

for i in range(s):
	imc = (p[i])/(a[i]**2)
	z[i] = round(imc, 2)
	
j = max(z)

if (j < 17):
	sit = "MUITO ABAIXO DO PESO"
elif (j >= 17 and j <= 18.49):
	sit = "ABAIXO DO PESO"
elif (j >= 18.50 and j <= 24.99):
	sit = "PESO NORMAL"
elif (j >= 25 and j <= 29.99):
	sit = "ACIMA DO PESO"
elif (j >= 30 and j <= 34.99):
	sit = "OBESIDADE"
elif (j >= 35 and j <= 39.99):
	sit = "OBESIDADE SEVERA"
elif (j >= 40):
	sit = "OBESIDADE MORBIDA"