from numpy import*
nf = array(eval(input("Nota Final: ")))
rp = 0

for i in range(size(nf)):
	if(nf[i] < 5):
		rp = rp + 1

a = 0
b = zeros(rp, dtype = int)
for i in range(size(nf)):
	if(nf[i] < 5):
		b[a] = i
		a = a + 1
				
print(rp)
print(b)
	
#nf >= 5.0
#print(rp) = ?
#