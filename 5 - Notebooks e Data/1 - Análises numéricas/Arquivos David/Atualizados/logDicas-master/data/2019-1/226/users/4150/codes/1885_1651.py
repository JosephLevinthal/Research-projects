from numpy import*

v = input("digite: ").split(',')

soma1 = 0
soma2 = 0
soma3 = 0
soma4 = 0
soma5 = 0
soma6 = 0

for i in range(size(v)):
	if v[i] == "MC":
		soma1 = soma1 + 1
	elif v[i] == "C":
		soma2 = soma2 + 1
	elif v[i] == "CM":
		soma3 = soma3 + 1
	elif v[i] == "EM":
		soma4 = soma4 + 1
	elif v[i] == "E":
		soma5 = soma5 + 1
	else:
		v[i] == "ME"
		soma6 = soma6 + 1
	i = i + 1
	
if soma1>soma2 and soma1>soma3 and soma1>soma4 and soma1>soma5 and soma1>soma6:
	print(soma1)
elif soma2>soma1 and soma2>soma3 and soma2>soma4 and soma2>soma5 and soma2>soma6:
	print(soma2)
elif soma3>soma1 and soma3>soma2 and soma3>soma4 and soma3>soma5 and soma3>soma6:
	print(soma3)
elif soma4>soma1 and soma4>soma2 and soma4>soma3 and soma4>soma5 and soma4>soma6:
	print(soma4)
elif soma5>soma1 and soma5>soma2 and soma5>soma3 and soma5>soma4 and soma5>soma6:
	print(soma5)
else:
	soma6>soma1 and soma6>soma2 and soma6>soma3 and soma6>soma4 and soma6>soma5
	print(soma6)

n = zeros(6, dtype=int)	
a = 0
for i in range(size(v)):
	if v[i] == "MC":
		n[0] = n[0] + 1
	elif v[i] == "C":
		n[1] = n[1] + 1
	elif v[i] == "CM":
		n[2] = n[2]+1
	elif v[i] == "EM":
		n[3] = n[3] + 1
	elif v[i] == "E":
		n[4] = n[4] + 1
	else:
		v[i] == "ME"
		n[5] = n[5] + 1
	a = a + 1

print(n)


		
	
	