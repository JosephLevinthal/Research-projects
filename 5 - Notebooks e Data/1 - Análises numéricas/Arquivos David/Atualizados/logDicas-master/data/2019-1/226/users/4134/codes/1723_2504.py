v = int(input("Virus: "))
l = int(input("leucocitos: "))
pv = int(input("proliferaçao dos virus"))
pl = int(input("proliferaçao dos leucocitos: "))
t = 0
while (2*v >= l):
	v = v*(1+(pv/100))
	l = l*(1+(pl/100))
	t = t + 1 
print(t)
	
