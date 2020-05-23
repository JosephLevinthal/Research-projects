from numpy import *
al=array(eval(input("notas:")))
x=sort(al)
c=x[1:5]
a=sum(c)/size(c)
print(round(a,2))