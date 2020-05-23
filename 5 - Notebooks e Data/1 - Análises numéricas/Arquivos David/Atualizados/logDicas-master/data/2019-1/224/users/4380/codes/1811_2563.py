from numpy import *
notas=array(eval(input("nota dos vagabundo: ")))
ne=0
while (size(notas)>1):
	nm=0
	for ne in notas:
		if (ne>=5 and ne<7):
			nm=nm+1
	print(nm)
	notas=array(eval(input("nota dos vagabundo: ")))
	