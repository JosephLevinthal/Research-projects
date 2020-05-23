from numpy import*

barca = array(eval(input("gol:")))
real = array(eval(input("gol:")))

x = zeros(3, dtype= int)

for i in range(size(barca)):
	if barca[i] >real[i]:
		x[0] = x[0] +1
	elif barca[i] == real[i]:
		x[1] = x[1] + 1
	elif barca[i] < real[i]:
		x[2] = x[2] + 1 
	
print(x)