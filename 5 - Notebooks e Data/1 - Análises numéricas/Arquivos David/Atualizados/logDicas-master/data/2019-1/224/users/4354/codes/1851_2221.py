from math import *
from numpy import *
mtr = array(eval(input("digite a matriz: ")))
c = mtr.shape [1]
l = mtr.shape [0]
s = 0
for i in range(l):
	s = s + min(mtr[i,:])
media = s/l
print(round(media,2))