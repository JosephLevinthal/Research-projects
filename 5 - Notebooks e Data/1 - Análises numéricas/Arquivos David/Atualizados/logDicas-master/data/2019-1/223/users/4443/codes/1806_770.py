from numpy import *
p1 = input("Digite a palavra 1: ")
p2 = input("Digite a palavra 2: ")
p1 = p1.upper()
p2 = p2.upper()
v1 = zeros(26, dtype=int)
for i in p1:
	if(i == "A"):
		v1[0] = v1[0] + 1
	elif(i == "B"):
		v1[1] = v1[1] + 1
	elif(i == "C"):
		v1[2] = v1[2] + 1
	elif(i == "D"):
		v1[3] = v1[3] + 1
	elif(i == "E"):
		v1[4] = v1[4] + 1
	elif(i == "F"):
		v1[5] = v1[5] + 1
	elif(i == "G"):
		v1[6] = v1[6] + 1
	elif(i == "H"):
		v1[7] = v1[7] + 1
	elif(i == "I"):
		v1[8] = v1[8] + 1
	elif(i == "J"):
		v1[9] = v1[9] + 1
	elif(i == "K"):
		v1[10] = v1[10] + 1
	elif(i == "L"):
		v1[11] = v1[11] + 1
	elif(i == "M"):
		v1[12] = v1[12] + 1
	elif(i == "N"):
		v1[13] = v1[13] + 1
	elif(i == "O"):
		v1[14] = v1[14] + 1
	elif(i == "P"):
		v1[15] = v1[15] + 1
	elif(i == "Q"):
		v1[16] = v1[16] + 1
	elif(i == "R"):
		v1[17] = v1[17] + 1
	elif(i == "S"):
		v1[18] = v1[18] + 1
	elif(i == "T"):
		v1[19] = v1[19] + 1
	elif(i == "U"):
		v1[20] = v1[20] + 1
	elif(i == "V"):
		v1[21] = v1[21] + 1
	elif(i == "W"):
		v1[22] = v1[22] + 1
	elif(i == "X"):
		v1[23] = v1[23] + 1
	elif(i == "Y"):
		v1[24] = v1[24] + 1
	elif(i == "Z"):
		v1[25] = v1[25] + 1
v2 = zeros(26, dtype=int)
for i in p2:
	if(i == "A"):
		v1[0] = v1[0] - 1
	elif(i == "B"):
		v1[1] = v1[1] - 1
	elif(i == "C"):
		v1[2] = v1[2] - 1
	elif(i == "D"):
		v1[3] = v1[3] - 1
	elif(i == "E"):
		v1[4] = v1[4] - 1
	elif(i == "F"):
		v1[5] = v1[5] - 1
	elif(i == "G"):
		v1[6] = v1[6] - 1
	elif(i == "H"):
		v1[7] = v1[7] - 1
	elif(i == "I"):
		v1[8] = v1[8] - 1
	elif(i == "J"):
		v1[9] = v1[9] - 1
	elif(i == "K"):
		v1[10] = v1[10] - 1
	elif(i == "L"):
		v1[11] = v1[11] - 1
	elif(i == "M"):
		v1[12] = v1[12] - 1
	elif(i == "N"):
		v1[13] = v1[13] - 1
	elif(i == "O"):
		v1[14] = v1[14] - 1
	elif(i == "P"):
		v1[15] = v1[15] - 1
	elif(i == "Q"):
		v1[16] = v1[16] - 1
	elif(i == "R"):
		v1[17] = v1[17] - 1
	elif(i == "S"):
		v1[18] = v1[18] - 1
	elif(i == "T"):
		v1[19] = v1[19] - 1
	elif(i == "U"):
		v1[20] = v1[20] - 1
	elif(i == "V"):
		v1[21] = v1[21] - 1
	elif(i == "W"):
		v1[22] = v1[22] - 1
	elif(i == "X"):
		v1[23] = v1[23] - 1
	elif(i == "Y"):
		v1[24] = v1[24] - 1
	elif(i == "Z"):
		v1[25] = v1[25] - 1
p=0
n=0
i = 0		
for num in v1:
	if(num > 0):
		p = p+1
	elif(num < 0):
		n = n+1
if(p+n >0):
	print(v1)
	print(0)
else:
	print(v1)
	print(1)	