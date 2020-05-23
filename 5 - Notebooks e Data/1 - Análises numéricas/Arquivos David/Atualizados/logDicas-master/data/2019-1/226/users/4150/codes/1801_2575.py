from numpy import*


v = array(eval(input("qual?" ))).upper()
x =  zeros(3, dtype=int)

for i in v:
	if i == "'TV'":
		x[0] = x[0]+1
	elif i == "'NETFLIX'":
		x[1] = x[1] + 1
	elif i == "'YOUTUBE'":
		x[2] = x[2] + 1
print(x)