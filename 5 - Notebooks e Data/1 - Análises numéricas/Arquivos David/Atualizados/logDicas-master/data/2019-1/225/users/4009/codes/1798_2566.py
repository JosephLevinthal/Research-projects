from numpy import*
import numpy as np
D = array(eval(input("Dias de semana:  ")))
a = np.zeros(6)
for i in D:
	a[i-2]+=1
a =(a/len(D))*100
for i in range(len(a)):
	a[i] = round(a[i],1)
print(a)