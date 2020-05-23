from numpy import*
cont = zeros(6 , dtype=int)
var = input("tom de pele? ").upper().split(",")
for i in range(size(var)):
	if (var[i] == "MC"):
		cont[0] = cont[0]+1
	if (var[i] == "C"):
		cont[1] = cont[1] + 1
	if (var[i] == "CM"):
		cont[2] = cont[2] + 1
	if (var[i] == "EM"):
		cont[3] = cont[3] + 1
	if (var[i] == "E"):
		cont[4] = cont[4] + 1
	if (var[i] == "ME"):
		cont[5] = cont[5] + 1
print(2)
print(cont)