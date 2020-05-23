from numpy import *
from numpy.linalg import *


t = array(eval(input("Tabuleiro: ")))
a = t.shape[0]
b = t.shape[1]

mov = input("Movimentos: ")
x = 0
y = 0
mo = 0
hp = 100

for i in mov:
	if i == "A":
		if x-1 != -1:
			if t[y,x-1] != 33:
				x -= 1
	elif i == "D":
		if x + 1 != b:
			if t[y,x+1] != 33:
				x += 1
	elif i == "W":
		if y - 1 != -1:
			if t[y-1,x] != 33:
				y -= 1
	elif i == "S":
		if y + 1 != a:
			if t[y+1,x] != 33:
				y += 1
	if t[y,x] == 11:
		mo += 1
		t[y,x] = 0
	elif t[y,x] == 22:
		hp -= 5
print("posicao x: ",x)
print("posicao y: ",y)
print("moedas: ",mo)
print("life: ",hp)