from numpy import *

v = array(eval(input("Insira o vetor: ")))

v1 = zeros(6)

s = 0
t = 0
qa = 0
qi = 0
se = 0
sa = 0

for x in v:
	if(x == 2):
		s = s + 1
	elif(x == 3):
		t = t + 1
	elif(x == 4):
		qa = qa + 1
	elif(x == 5):
		qi = qi + 1
	elif(x == 6):
		se = se + 1
	elif(x == 7):
		sa = sa + 1

v1[0] = round(s / size(v) * 100, 1)
v1[1] = round(t / size(v) * 100, 1)
v1[2] = round(qa / size(v) * 100, 1)
v1[3] = round(qi / size(v) * 100, 1)
v1[4] = round(se / size(v) * 100, 1)
v1[5] = round(sa / size(v) * 100, 1)

print(v1)