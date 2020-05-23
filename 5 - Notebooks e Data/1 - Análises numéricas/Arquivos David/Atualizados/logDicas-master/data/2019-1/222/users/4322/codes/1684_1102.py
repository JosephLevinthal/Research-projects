from math import *
# Olhando para a figura, percebemos que ela é uma junção de
# Uma semiesfera superior, um cilindro no meio e outra semiesfera inferior.

# Temos 4 formulas de volumes aqui:

# Volume da esfera de raio r: 
# 									Ve = (4/3)*pi*r**3
#
# Volume de uma semiesfera é metade do volume de uma esfera, então
# Volume da semiesfera de raio r: 
# 									Vse = (2/3)*pi*r**3

# Volume do cilindro de altura h e raio r:
#									Vc = pi*r**2*h

# Volume da calota esférica de altura h e raio r:
#									Vca = (1/3)*pi*h**2*(3r - h)

# Caso 1 - Se o combustível estiver na parte inferior do tanque, ou seja,
# abaixo do cilindro no meio, então o volume do combustivel no maximo
# o volume da semiesfera infeiror, no entanto, o h sera determinado
# pela altura do combustivel. Então temos:
#									V = (1/3)*pi*h**2 * (3r - h)

# Caso 2 - Se o combustível estiver entre o começo e o fim do cilindro do meio, 
# temos que o volume será a soma do volume da semiesfera debaixo e 
# mais o que sobrar de combustível no cilindro, que terá altura (h - r). 
# Onde r é a altura da semiesfera.
# Então o volume de combustível é:
#									V = Vse + Vc = (2/3)*pi*r**3 + pi*r**2*(h - r)

# Caso 3 - Se o combustível estiver entre a semiesfera superior e o topo, 
# então teremos que somar o volume da semiesfera inferior mais o cilindro e mais o que sobrar de combustivel
# na semiesfera supeior, ou seja,  se o volume for o tanque todo, temos
# somente que somar o volume de duas semiesfera e o de um cilindro, mas
# somar duas o volume de duas semiesferas é o mesmo que somar uma esfera toda,
# então usaremos o volume da esfera neste. Temos que lembrar que se o volume
# não for o tanque todo, então teremos que subtrair o volume do ar dentro do tanque,
# ou seja, o que tá sobrando sem combustível. Para isto, vamos levar em consideração
# que o a altura do volume do ar é (H - h), certo? Pois, imagina aí se o h tiver quase
# no teto, o que sobra é de ar é a diferença (H - h) de altura. Vamos aos cálculos:

# Somando todos os volumes temos:
#										VTotal = Ve + Vc = (4/3)*pi*r**3 + pi*r**2*(H - 2*r)
# Calculando o volume do ar temos:
# Só substitui a altura (H - h) na formula do volume da calota.
#										Var = (1/3)*pi*(H-h)**2 * (3*r - (H-h))
# 
# Sabemos que o volume do combustível será Vtotal - Var, então:
#										V = (4/3)*pi*r**3 + pi*r**2*(H - 2*r) - (1/3)*pi*(H-h)**2 * (3*r - (H-h))


H = float(input("Altura total do tanque: "))
h = float(input("Nivel de combustivel do tanque: "))
r = float(input("Raio: "))

print("Entradas: {} , {} , {}".format(H,h,r))


# Verificar se as entradas são válidas
if (H < 0) or (h < 0) or (r < 0) or (H < h) or (H < 2*r):
	print("Entradas invalidas")
else:
	if (h < r): #Caso 1
		V=(1/3)*pi*(h**2)*(3*r - h)
	elif (h < H - r): #Caso 2
		V=(2/3)*pi*r**3 + pi*r**2*(h - r)
	elif (h <= H): #Caso 3
		V=(4/3)*pi*(r**3) + pi*(r**2)*(H - 2*r) - (1/3)*pi*((H-h)**2) * (3*r - (H-h))
	
	print("Volume:",round(V*1000,3),"litros")
	# V*1000 porque 1 metro cubico equivale a 1000 litros