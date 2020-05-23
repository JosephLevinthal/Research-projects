from numpy import*
p = array(eval(input("peso: ")))
a = array(eval(input("altura: ")))
n = size(p)
t = zeros(n)
y = 0
for x in p:
	t[y] = round(x/(a[y]**2) , 2)
	y = y + 1
print(t)
print("O MAIOR IMC DA TURMA EH:", max(t))
if max(t) < 17:
	print("MUITO ABAIXO DO PESO")
elif 17<max(t)<=18.49:
	print("ABAIXO DO PESO")
elif 18.5<max(t)<=24.99:
	print("PESO NORMAL")
elif 25<max(t)<=29.99:
	print("ACIMA DO PESO")
elif 30<max(t)<=34.99:
	print("OBESIDADE")
elif 35<max(t)<=39.99:
	print("OBESIDADE SEVERA")
elif max(t)>40:
	print("OBESIDADE MORBIDA")