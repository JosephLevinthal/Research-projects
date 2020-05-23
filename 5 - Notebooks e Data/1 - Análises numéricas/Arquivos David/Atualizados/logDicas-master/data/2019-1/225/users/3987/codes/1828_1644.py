from numpy import*

n = array(eval(input("notas:")))
vn = zeros(size(n), dtype=int)
rp = 0
for i in range(size(n)):
	if(n[i] < 5):
		rp = rp + 1
print(rp)

for i in range(n,0,-1):
	vn[i] = vn[i] + 1
print(vn)
		
	


	
