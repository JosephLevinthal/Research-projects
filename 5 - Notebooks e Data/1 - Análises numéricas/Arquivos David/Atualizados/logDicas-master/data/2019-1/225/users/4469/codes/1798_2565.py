from numpy import*

v1 = array(eval(input()))
v2 = array(eval(input()))
ch = int(input())

v3 = zeros(3, dtype = int)

a = 0
rn = 0
rf = 0

i = 0
while(i < size(v1)):
	if(v1[i] >= 5) and (v2[i] >= (ch * 75)/100):
		a = a + 1
	elif(v1[i] < 5):
		rn = rn + 1
	elif(v2[i] < (ch * 75)/100):
		rf = rf + 1
	i = i + 1

v3[0] = a
v3[1] = rn
v3[2] = rf

print(v3)