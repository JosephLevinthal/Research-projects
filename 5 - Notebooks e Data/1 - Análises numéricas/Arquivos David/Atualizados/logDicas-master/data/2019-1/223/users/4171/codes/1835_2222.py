from numpy import *
from numpy.linalg import *

a = int(input(""))

l1=array(eval(input()))
l2=array(eval(input()))
l3=array(eval(input()))

tra = l1[0]+l2[1]+l3[2]
tra2 = l1[2]+l2[1]+l3[0]

print(tra -tra2)