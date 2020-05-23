from numpy import*
from numpy.linalg import*

v1 = array(eval(input("Digite a cidade: ")))
v2 = array(eval(input("Digite a cidade: ")))
tempo = array([[0,2,11,6,15,11,1],[2,0,7,12,4,2,15],[11,7,0,11,8,3,13],[6,12,11,0,10,2,1],[15,4,8,10,0,5,13],[11,2,3,2,5,0,14],[1,15,13,1,13,14,0]])

a = 0
while	(v2 != -1 and v1 != 1):
		i = (v1%10) - 1
		j = (v2%10) - 1
		a = a + tempo[i,j]
		v1 = v2
	
		v2 = array(eval(input("Digite a cidade: ")))	
print(a)
	