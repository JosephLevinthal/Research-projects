from numpy import*

v1 = array(eval(input()))

v2 = zeros(6)

d2 = d3 = d4 = d5 = d6 = d7 = 0
for i in v1:
	if(i == 2):
		d2 = d2 + 1
	elif(i == 3):
		d3 = d3 + 1
	elif(i == 4):
		d4 = d4 + 1
	elif(i == 5):
		d5 = d5 + 1
	elif(i == 6):
		d6 = d6 + 1
	elif(i == 7):
		d7 = d7 + 1

v2[0] = round((d2 / size(v1)) * 100, 1)
v2[1] = round((d3 / size(v1)) * 100, 1)
v2[2] = round((d4 / size(v1)) * 100, 1)
v2[3] = round((d5 / size(v1)) * 100, 1)
v2[4] = round((d6 / size(v1)) * 100, 1)
v2[5] = round((d7 / size(v1)) * 100, 1)

print(v2)