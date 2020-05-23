from numpy import*
from numpy.linalg import*

v = array ([[1,-1,0,0],
			  [0,1,-1,0],
			  [0,0,1,0],
			  [1,0,0,1]])
a = array (v [:,0])
b = array (v [:,1])
c = array (v [:,2])
d = array (v [:,3])
r = array ([50,-120,350,870])
D = det (v)
for i in range(shape (v)[0]):
   if (i == 0):
      v [:,0] = r.T
      d1 = round(det (v),0)
   elif (i == 1):
      v [:,0] = a
      v [:,1] = r.T
      d2 = round(det (v),0)
   elif (i == 2):
      v [:,1] = b
      v [:,2] = r.T
      d3 = round(det(v),0)
   elif (i == 3):
      v [:,2] = c
      v [:,3] = r.T
      d4 = round(det (v),0)
resp = array ([d1/D,d2/D,d3/D,d4/D])
print (resp)