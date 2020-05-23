from numpy import*

s = input()

v1 = s.split(',')

am = pe = mg = sp = rs = 0
for i in v1:
	if(i.upper() == "AM"):
		am += 1
	elif(i.upper() == "PE"):
		pe += 1
	elif(i.upper() == "MG"):
		mg += 1
	elif(i.upper() == "SP"):
		sp += 1
	elif(i.upper() == "RS"):
		rs += 1

v2 = array([am, pe, mg, sp, rs])
print(max(v2))
print(v2)