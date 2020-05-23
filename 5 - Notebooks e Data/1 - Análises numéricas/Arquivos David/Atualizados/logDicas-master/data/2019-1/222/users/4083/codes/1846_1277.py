from numpy import*
from numpy.linalg import*

v1 = int(input("Digite a primeira cidade: "))
v2 = int(input("Digite a segunda cidade: "))
tempo = array([[0,2,11,6,15,11,1],[2,0,7,12,4,2,15],[11,7,0,11,8,3,13],[6,12,11,0,10,2,1],[15,4,8,10,0,5,13],[11,2,3,2,5,0,14],[1,15,13,1,13,14,0]])

if	(v1 == 111 ):
		v1 = 0
elif	(v1== 222):
		v1 = 1
elif	(v1 == 333):
		v1 = 2
elif	(v1== 444):
		v1 = 3
elif	(v1 == 555):
		v1 = 4
elif	(v1== 666):
		v1 = 5
elif	(v1 == 777):
		v1 = 6
		
if	(v2 == 111 ):
		v2 = 0
elif	(v2== 222):
		v2 = 1
elif	(v2 == 333):
		v2 = 2
elif	(v2== 444):
		v2 = 3
elif	(v2 == 555):
		v2 = 4
elif	(v2== 666):
		v2 = 5
elif	(v2 == 777):
		v2 = 6

b = tempo[v1,v2]
print(b)