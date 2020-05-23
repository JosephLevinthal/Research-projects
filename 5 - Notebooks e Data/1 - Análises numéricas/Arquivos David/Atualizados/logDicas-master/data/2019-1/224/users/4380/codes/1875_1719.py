from numpy import *
from numpy.linalg import *
notas=array(eval(input("matriz: ")))
ap=0
i=0
for i in range (shape(notas)[0]):
	media=(sum(notas[i,:]))/shape(notas)[0]
	if (media>=5):
		ap=ap+1
		i=i+1
	elif (media<5):
		ap=ap+0
		i=i+1
print(ap)