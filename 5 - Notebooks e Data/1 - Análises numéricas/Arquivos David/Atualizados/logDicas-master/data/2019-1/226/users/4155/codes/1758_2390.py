from numpy import *
tr = array(eval(input("b: ")))
maior_tr = max(tr)
i = 0
while(i<size(tr)):
	if(tr[i] == maior_tr):
		mes = i + 1
	i = i + 1
print(mes)