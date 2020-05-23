from numpy import*

day = array(eval(input("dias:")))
final = zeros(6, dtype = float)
x = zeros(6, dtype = float)

for i  in range(size(day)):
	if day[i] == 2:
		x[0] = x[0] +1 * 100/size(day) 
	elif day[i] == 3:
		x[1] = x[1] + 1* 100/size(day) 
	elif day[i] == 4: 
		x[2] = x[2] +1 * 100/size(day) 
	elif day[i] == 5:
		x[3] = x[3] +1  * 100/size(day)
	elif day[i] == 6:
		x[4] = x[4] +1 * 100/size(day) 
	elif day[i] == 7:
		x[5] = x[5] +1 * 100/size(day) 

a = round(x[0],1)
b = round(x[1],1)
c = round(x[2],1)
d = round(x[3],1)
e = round(x[4],1)
f = round(x[5],1)

final[0] = a
final[1] = b
final[2] = c
final[3] = d
final[4] = e
final[5] = f

print(final)