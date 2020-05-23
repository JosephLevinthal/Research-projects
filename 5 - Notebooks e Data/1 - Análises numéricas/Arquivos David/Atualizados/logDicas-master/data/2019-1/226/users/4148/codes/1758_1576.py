from numpy import*

v1 = array(eval(input("jogada 1: ")))
v2 = array(eval(input("jogada 2: "))) 

print(size(v1) + size(v2)/2)

i = 0
s1 = 0
s2 = 0

while i <=  size(v1):
	if(v1[1]==11 and v2[i] == 33) or (v1[i]==22 and v2==11) or (v1[i]==33 and v2[i]==22):
		s1 = s1 + 1
	elif(v1[i]==33 and v2[i] or v1[i]==11 and v2[i]==22 or v1[i] == 22 and v2[i] ==33):
		s2 = s2 +1
	else:
		print("empate")
	
print(size(v1))

if soma > soma2:
	print("EUSAPIA")
elif soma < soma2:
	print("BARSANULFO")
	
