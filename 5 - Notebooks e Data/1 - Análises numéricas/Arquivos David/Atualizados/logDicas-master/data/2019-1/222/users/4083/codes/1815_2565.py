from numpy import*

nota = array(eval(input("Digite as notas: ")))
frequencia = array(eval(input("Digite as frequencias: ")))
carga = int(input("carga horaria: "))
a = zeros(3, dtype=int)
a1 = 0
a2 = 0
a3 = 0
n = carga*(75/100)
for i in range(size(nota)):
	if	(nota[i] >= 5 and frequencia[i] >= n):
		a1 = a1 + 1
				
	elif (frequencia[i] < n):
			a3 = a3 + 1
		
	elif	(nota[i] < 5 ):
			a2 = a2 + 1
				
	
a[0] = a1
a[1] = a2
a[2] = a3
print(a)