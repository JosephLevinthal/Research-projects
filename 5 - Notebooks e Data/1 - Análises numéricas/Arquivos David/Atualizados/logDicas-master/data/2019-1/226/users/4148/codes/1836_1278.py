from numpy import*
from numpy.linalg import*



cidade1 = int(input())
cidade2 = int(input())

while(cidade2 != -1):
	acc+=[cidade1//111 - 1, cidade2//111-1]
	cidade1=cidade2
	cidade2 = int(input())
print(acc)