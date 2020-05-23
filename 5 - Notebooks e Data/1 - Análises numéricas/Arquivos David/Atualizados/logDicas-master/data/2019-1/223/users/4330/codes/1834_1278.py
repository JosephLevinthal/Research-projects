from numpy import*
from numpy.linalg import*

distance_city=array([
	[0,2,11,6,15,11,1],
	[2,0,7,12,4,2,15],
	[11,7,0,11,8,3,13],
	[6,12,11,0,10,2,1],
	[15,4,8,10,0,5,13],
	[11,2,3,2,5,0,14],
	[1,15,13,1,13,14,0]])

distance = 0 
cityA = int(input("cityA:"))
cityB = int(input("cityB:"))
while( cityB != -1):
	distance = distance_city[(cityA//100) - 1, (cityB//100) - 1] + distance
	cityA = cityB
	cityB = int(input("cityB:"))
print(distance)	



