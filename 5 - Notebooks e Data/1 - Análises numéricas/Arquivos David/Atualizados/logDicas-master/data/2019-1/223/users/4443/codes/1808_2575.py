from numpy import *
pref = array(eval(input("Digite uma das opcoes TV Netflix Youtube: ")))
vs = zeros(3, dtype=int)
for i in range(size(pref)):
	if(pref[i] == "TV"):
		vs[0] = vs[0] + 1
	elif(pref[i] == "NETFLIX"):
		vs[1] = vs[1] + 1	
	elif(pref[i] == "YOUTUBE"):
		vs[2] = vs[2] + 1
print(vs)	