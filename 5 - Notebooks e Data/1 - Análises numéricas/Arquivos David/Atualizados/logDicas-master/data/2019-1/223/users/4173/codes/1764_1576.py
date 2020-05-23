from numpy import*
a = eval(input())
b = eval(input())
va = array(a)
vb = array(b)
part = 0
ev = 0
bv = 0
while part < size(a):
	if (va[part] == 11) and (vb[part] == 22) or (va[part] == 22) and (vb[part] == 33) or (va[part] == 33) and (vb[part] == 11):
		bv += 1
	elif (vb[part] == 11) and (va[part] == 22) or (vb[part] == 22) and (va[part] == 33) or (vb[part] == 33) and (va[part] == 11):
		ev += 1
	elif (va[part] == vb[part]):
		bv +=0
		ev +=0
	part += 1
print(part)
if(ev > bv):
	print("EUSAPIA")
elif(bv > ev):
	print("BARSANULFO")
elif(ev == bv):
	print("EMPATE")
	
