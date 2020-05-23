from numpy import *
n = int(input("digite o numero: "))
################################
i = 0
s1 = 0
s2 = 1
z = zeros(n,dtype = int)
while(i<n):
	z[i] = s1
	s2 = s2 + s1
	s1 = s1 + s2
	i = i + 1
	# s1 par
###############################
i2 = 0
s3 = 0
s4 = 1
z2  = zeros(n,dtype = int)
while(i2<n):
	s4 = s4 + s3
	s3 = s3 + s4
	z2[i2] = s4
	i2 = i2 + 1

#################################
i3 = 0
i4 = 0
i5 = 0
z3 = zeros(n,dtype = int)
while(i5<n):
	if(i5%2 == 0):
		z3[i5] = z[i3]
		i4 = i4 + 0
		i3 = i3 + 1
	else:
		z3[i5] = z2[i4]
		i4 = i4 + 1
		i3 = i3 + 0
	i5 = i5 + 1
print(z3)

	
	