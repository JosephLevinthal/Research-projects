from numpy import*
from numpy.linalg import*
c = array(eval(input("c: ")))
i = 0
d = array([
	      [8,10,16],
	      [2,3,5],
	      [1,2,3]])

v = zeros(3)

v = dot(inv(d), c.T)
			  
print("centurion:", round(v[0], 0))
print("tribune:", round(v[1], 0))
print("senator:", round(v[2], 0))

if (v[0] == min(v)):
	print("centurion")
elif (v[1] == min(v)):
	print("tribune")
elif (v[2] == min(v)):
	print("senator")