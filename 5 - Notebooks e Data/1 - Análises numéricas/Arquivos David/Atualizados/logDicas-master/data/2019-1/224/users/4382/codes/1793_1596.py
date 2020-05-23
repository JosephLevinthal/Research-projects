from numpy import *
VN = array(eval(input(" vetor de notas:")))
i = 0
s = 0
siz = 0
while(i<size(VN)):
	if(VN[i]== min(VN)):
		s = s + 0
		siz = siz + 0
	else :
		s = s + VN[i]
		siz = siz + 1
	i = i + 1
M = s/siz
print(round(M,2))
