from numpy import *
from numpy.linalg import *

v = int (input ("digite: "))
a = v//100 -1
b = 0
mat = array([[0, 2, 11,6,15,11,1],
            [2, 0, 7, 12, 4, 2, 15],
            [11, 7, 0, 11, 8, 3, 13],
            [6, 12, 11, 0, 10, 2, 1],
            [15, 4, 8, 10, 0, 5, 13],
            [11, 2, 3, 2, 5, 0, 14],
            [1, 15, 13, 1, 13, 14, 0]])

d = 0
if (v != -1):
   v2 = int (input ("digite: "))
   while (v2 != -1):
      b = v2//100 - 1
      d = d + mat [a,b]
      a = a * 0
      a = v2//100 - 1
      b = b * 0
      v2 = int (input ("digite: "))
print (d)