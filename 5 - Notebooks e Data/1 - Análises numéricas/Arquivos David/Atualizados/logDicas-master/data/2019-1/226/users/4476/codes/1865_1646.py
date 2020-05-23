
v = array(eval(input("Dgt: ")))

sl = 0

for i in range(v):
	if(v[i] <= 50):
		sl = sl + 1

v2 = zeros(sl, dtype=int)
a = 0
b = 0

for i in range(v):
	if(v[i] <= 50):
		v2[0] = v[i]
		
print(sl)
		
		