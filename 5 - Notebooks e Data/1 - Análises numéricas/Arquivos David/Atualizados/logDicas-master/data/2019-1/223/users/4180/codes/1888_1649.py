from numpy import*

cores = input("cores dos olhos:")
cores = cores.split(',')

p = 0
c = 0 
m = 0
v = 0
a = 0

for i in range(size(cores)):
	if (cores[i] == "P"):
		p = p + 1
	elif (cores[i] == "C" ):
		c = c + 1
	elif (cores[i] == "M"):
		m = m + 1
	elif (cores[i] == "V"):
		v = v + 1
	elif (cores[i] == "A"):
		a = a + 1

cliente = zeros(5, dtype=int)

cliente[0] = p
cliente[1] = c
cliente[2] = m
cliente[3] = v
cliente[4] = a

print(max(cliente))
print(cliente)
		
		
		