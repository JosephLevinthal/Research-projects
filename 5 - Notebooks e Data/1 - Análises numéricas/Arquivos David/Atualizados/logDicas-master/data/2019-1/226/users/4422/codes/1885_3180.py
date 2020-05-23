from numpy import*
v = array(eval(input('v: ')))
new = zeros(4, dtype=int)

for x in v:
	if x == 1:
		new[0] = new[0] + 1
	elif x == 2:
		new[1] = new[1] + 1
	elif x == 3:
		new[2] = new[2] + 1
	elif x == 4:
		new[3] = new[3] + 1

print(new)

		