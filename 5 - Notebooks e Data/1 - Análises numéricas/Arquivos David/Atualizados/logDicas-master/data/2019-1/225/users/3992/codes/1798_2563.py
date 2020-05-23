from numpy import*
v = array(eval(input("media:")))

while (size(v)>1):
	a = 0
	for elemento in v:
		if (elemento >= 5 and elemento < 7):
			a = a + 1
	v = array(eval(input("media: ")))
	print(a)