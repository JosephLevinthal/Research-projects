from numpy import *
from numpy.linalg import *
t = array(eval(input("Digite o tabuleiro: ")))
m = input("Digite os movimentos: ").upper()
ct = 0
lt = 0
moeda = 0
life = 100
for x in m:
	if (x == "A"):
		ct = ct - 1
		if (ct < 0 or ct >= shape(t)[1]):
			ct = ct + 1
	elif (x == "D"):
		ct = ct + 1
		if (ct < 0 or ct >= shape(t)[1]):
			ct = ct - 1
	elif (x == "W"):
		lt = lt - 1
		if (lt < 0 or lt >= shape(t)[1]):
			lt = lt + 1
	elif (x == "S"):
		lt = lt + 1
		if (lt < 0 or lt >= shape(t)[1]):
			lt = lt - 1
	if(t[lt,ct] == 33):
		if (x == "A"):
			ct = ct + 1
		elif (x == "D"):
			ct = ct - 1
		elif (x == "W"):
			lt = lt + 1
		elif (x == "S"):
			lt = lt - 1		
	if (t[lt,ct] == 11):
		moeda = moeda + 1
		t[lt,ct] = 0
		t[lt,ct] == 0
	elif (t[lt,ct] == 22):
		life = life - 5
	
print("posicao x: ", ct)
print("posicao y: ", lt)
print("moedas: ", moeda)
print("life: ", life)
		
