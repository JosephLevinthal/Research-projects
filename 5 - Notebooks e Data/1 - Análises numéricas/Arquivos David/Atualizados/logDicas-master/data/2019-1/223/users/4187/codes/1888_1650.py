from numpy import*

cores = input("cores de cabelo:")
cores = cores.split(',')

p = 0
c = 0
r = 0
l = 0
b = 0

for i in range(size(cores)):
	if (cores[i] == "P"):
		p = p + 1
	elif (cores[i] == "C"):
		c = c + 1
	elif( cores[i] == "R"):
		r = r + 1
	elif(cores[i] == "L"):
		l = l + 1
	elif(cores[i] == "B"):
		b = b + 1

cliente = zeros(5,dtype=int)

cliente[0] = p
cliente[1] = c
cliente[2] = r
cliente[3] = l
cliente[4] = b


print(max(cliente))
print(cliente)