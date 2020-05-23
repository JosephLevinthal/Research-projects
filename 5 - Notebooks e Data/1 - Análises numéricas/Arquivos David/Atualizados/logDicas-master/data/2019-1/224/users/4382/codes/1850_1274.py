from numpy import *
from numpy.linalg import *
num=int(input("digite os numbers: "))
dc=zeros((num,num),dtype=int)
for i in range (num):
	for j in range (i,num):
		dc[i,j]=i+1
		dc[j,i]=i+1
print(dc)