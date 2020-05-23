from numpy import *
# Sequencia de jogadas de Eusapia
v1 = array(eval(input("Insira um vetor nigga: ")))
# Jogadas correspondentes de Barsanulfo
v2 = array(eval(input("Insira um vetor : ")))

pedra = 11
papel = 22
tesoura = 33

print(size(v2))

i = 0
somae = 0
somab = 0
somai = 0
while(i < size(v2)):
	if(v1[i] == v2[i]):
		somai = somai + 1
	elif((v1[i] == 11) and (v2[i] == 33) or (v1[i] == 22) and (v2[i] == 11) or (v1[i] == 33) and (v2[i] == 22)):
		somae = somae + 1
	else:
		somab = somab + 1
	i = i + 1
if(somae > somab):
	print("EUSAPIA")
elif(somae == somab):
	print("EMPATE")
else:
	print("BARSANULFO")