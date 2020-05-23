from numpy import*
v = array(eval(input("vetor: ")))
n = array(eval(input("vetor: ")))
m = 0
e = 0
b = 0
while(m<size(v)):
	if((v[m]==22 and n[m]==11) or (v[m]==11 and n[m]==33) or (v[m]==33 and n[m]==22)):
		e = e+1
	elif((n[m]==22 and v[m]==11) or (n[m]==11 and v[m]==33) or (n[m]==33 and v[m]==22)):
		b = b+1
	m =m+1
if(e>b):
	print(m)
	print("EUSAPIA")
elif(b>e):
	print(m)
	print("BARSANULFO")
else:
	print(m)
	print("EMPATE")