from numpy import*
x = array(eval(input("vetor medias finais: ")))

a = 0 #aprovados
m = 0 #monitores

while size(x) > 1:
	a = 0
	m = 0
	for i in x:
		if i >= 5:
			a = a + 1
			if i >= 7:
				m = m + 1
	print(a - m)
	x = array(eval(input("vetores medias finais: ")))
