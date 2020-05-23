from numpy import*
from  math import*
v = array(eval(input("coloque ai:")))
b = sum(v)/size(v)
i = 0
for r in v:
	i = i+(r-b)**2
i=sqrt(i/(size(v)-1))
print(round(i, 3))