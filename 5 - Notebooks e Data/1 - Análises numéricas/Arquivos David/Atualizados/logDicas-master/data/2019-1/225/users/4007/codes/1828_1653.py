from numpy import*
p = input("nacionalidades das pessoas: ").upper().split(',')

t = zeros(5, dtype=int)
for i in range(size(p)):
	if (p[i] == 'AR'):
		t[0] = t[0] + 1
	elif (p[i] == 'BR'):
		t[1] = t[1] + 1
	elif (p[i] == 'CL'):
		t[2] = t[2] + 1
	elif (p[i] == 'CO'):
		t[3] = t[3] + 1
	elif (p[i] == 'UY'):
		t[4] = t[4] + 1
print(max(t))	
print(t)









	