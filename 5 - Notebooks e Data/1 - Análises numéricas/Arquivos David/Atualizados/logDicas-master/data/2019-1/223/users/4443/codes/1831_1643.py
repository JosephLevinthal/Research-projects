from numpy import *
nota = array(eval(input("Digite as notas dos estudantes: ")))
aprovados = 0
for nta in nota:
	if(nta >=5):
		aprovados = aprovados +1

vi = zeros(aprovados, dtype=int)
ve = 0
vs = 0
for nta in nota: 		
	if(nota[ve]>=5):
		vi[vs] = ve
		ve = ve+1
		vs = vs+1
	else:
		ve = ve+1
		vs = vs
print(aprovados)
print(vi)