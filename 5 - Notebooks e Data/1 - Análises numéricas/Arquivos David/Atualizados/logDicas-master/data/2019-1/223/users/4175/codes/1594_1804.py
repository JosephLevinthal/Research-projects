from math import *
XA = float(input())
YA = float(input())
XB = float(input())
YB = float(input())

A = (XA,YA)
B = (XB,YB)

da = (XB-XA)**2
db = (YB-YA)**2

dab = da + db
DAB = sqrt(dab)
print(round(DAB,3))