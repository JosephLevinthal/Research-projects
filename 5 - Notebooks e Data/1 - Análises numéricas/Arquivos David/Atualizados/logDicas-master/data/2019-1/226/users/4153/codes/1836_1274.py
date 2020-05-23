from numpy import *
from numpy.linalg import*

n = int (input ("insira: "))
j = 0
c = 1
v = zeros (((n,n)),dtype=int)
for i in range (n):
   for j in range (n):
      if (i == j):
         v [i,j] = i + 1
      elif (i > j):
         v [i,j] = j + 1
      elif ( i < j):
         v [i,j] = i + 1
print (v)