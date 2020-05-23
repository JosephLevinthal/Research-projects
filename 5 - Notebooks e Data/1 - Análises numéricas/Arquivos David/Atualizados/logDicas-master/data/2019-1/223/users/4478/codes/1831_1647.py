from numpy import*
v1 = eval(input("alunos: "))

aprovados = 0


for i in range(0, size(v1)):
	if(v1[i]>=70):
		aprovados = aprovados + 1
print(aprovados)
vcont = zeros(aprovados, dtype=int)
for i in range(0, size(v1)):
	if(v1[i] >= 70):
		vcont = vcont+1
	
print(vcont)
