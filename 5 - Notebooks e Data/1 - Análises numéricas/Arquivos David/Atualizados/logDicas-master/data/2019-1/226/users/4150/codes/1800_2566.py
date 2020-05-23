from numpy import*

v = array(eval(input("digite: ")))

x = zeros(6, dtype=float)
s = 0 
t = 0
q = 0
qui = 0 
sex = 0 
sab = 0


for i in range(size(v)):
	if v[i] == 2:
		s = s + 1
	elif v[i] == 3:
		t = t + 1
	elif v[i] == 4:
		q = q + 1
	elif v[i] == 5:
		qui= qui + 1
	elif v[i] == 6:
		sex = sex + 1
	elif v[i] == 7:
		sab = sab + 1
	
x[0] = round(s/size(v)*100,1)
x[1] = round(t/size(v)*100,1)
x[2] = round(q/size(v)*100,1)
x[3] = round (qui/size(v)*100,1)
x[4] = round(sex/size(v)*100,1)
x[5] = round (sab/size(v)*100,1)
print(x)
		
	