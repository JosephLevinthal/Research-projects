from numpy import *
v = array(eval(input("vetor: ")))
M = ((v[0]**1/3 + v[1]**1/3 + v[2]**1/3)/size(v))**3
print(round(M, 2)