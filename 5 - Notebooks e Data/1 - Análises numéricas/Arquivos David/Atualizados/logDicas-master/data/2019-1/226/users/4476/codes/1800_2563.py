from numpy import *
v = array(eval(input("Digite: ")))



while (size(v) > 1):
	m = 0
	for i in v:
		if (i >= 5) and (i < 7):
			m = m + 1
	print(m)
	v = array(eval(input("Digite: ")))