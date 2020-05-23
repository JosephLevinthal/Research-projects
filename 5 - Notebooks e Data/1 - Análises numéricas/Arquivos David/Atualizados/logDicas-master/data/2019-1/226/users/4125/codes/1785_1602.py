from numpy import*
v = array(eval(input("digite os tempos: ")))
i = 0
ins = 0
while(i<size(v)):
	if(v[i]>v[ins]):
		ins = ins + 1
		i = i+1
	else:
		i = i + 1
print(ins)