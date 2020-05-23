from numpy import * 
string = input("digite a palavra: ")
string2 = input("digite a segunda palavra: ")
string = string.upper()
string2 = string2.upper()
z = zeros(26,dtype = int)
i = 0
while(i < len(string)):
	if(string[i] == "A"):
		z[0] = z[0] + 1
	if(string[i] == "B"):
		z[1] = z[1] + 1
	if(string[i] == "C"):
		z[2] = z[2] + 1
	if(string[i] == "D"):
		z[3] = z[3] + 1
	if(string[i] == "E"):
		z[4] = z[4] + 1
	if(string[i] == "F"):
		z[5] = z[5] + 1
	if(string[i] == "G"):
		z[6] = z[6] + 1
	if(string[i] == "H"):
		z[7] = z[7] + 1
	if(string[i] == "I"):
		z[8] = z[8] + 1
	if(string[i] == "J"):
		z[9] = z[9] + 1
	if(string[i] == "K"):
		z[10] = z[10] + 1
	if(string[i] == "L"):
		z[11] = z[11] + 1
	if(string[i] == "M"):
		z[12] = z[12] + 1
	if(string[i] == "N"):
		z[13] = z[13] + 1
	if(string[i] == "O"):
		z[14] = z[14] + 1
	if(string[i] == "P"):
		z[15] = z[15] + 1
	if(string[i] == "Q"):
		z[16] = z[16] + 1
	if(string[i] == "R"):
		z[17] = z[17] + 1
	if(string[i] == "S"):
		z[18] = z[18] + 1
	if(string[i] == "T"):
		z[19] = z[19] + 1
	if(string[i] == "U"):
		z[20] = z[20] + 1
	if(string[i] == "V"):
		z[21] = z[21] + 1
	if(string[i] == "W"):
		z[22] = z[22] + 1
	if(string[i] == "X"):
		z[23] = z[23] + 1
	if(string[i] == "Y"):
		z[24] = z[24] + 1
	if(string[i] == "Z"):
		z[25] = z[25] + 1
	i = i + 1
################################
i2 = 0
z2 = zeros(26,dtype = int)
while(i2 < len(string2)):
	if(string2[i2] == "A"):
		z2[0] = z2[0] + 1
	if(string2[i2] == "B"):
		z2[1] = z2[1] + 1
	if(string2[i2] == "C"):
		z2[2] = z2[2] + 1
	if(string2[i2] == "D"):
		z2[3] = z2[3] + 1
	if(string2[i2] == "E"):
		z2[4] = z2[4] + 1
	if(string2[i2] == "F"):
		z2[5] = z2[5] + 1
	if(string2[i2] == "G"):
		z2[6] = z2[6] + 1
	if(string2[i2] == "H"):
		z2[7] = z2[7] + 1
	if(string2[i2] == "I"):
		z2[8] = z2[8] + 1
	if(string2[i2] == "J"):
		z2[9] = z2[9] + 1
	if(string2[i2] == "K"):
		z2[10] = z2[10] + 1
	if(string2[i2] == "L"):
		z2[11] = z2[11] + 1
	if(string2[i2] == "M"):
		z2[12] = z2[12] + 1
	if(string2[i2] == "N"):
		z2[13] = z2[13] + 1
	if(string2[i2] == "O"):
		z2[14] = z2[14] + 1
	if(string2[i2] == "P"):
		z2[15] = z2[15] + 1
	if(string2[i2] == "Q"):
		z2[16] = z2[16] + 1
	if(string2[i2] == "R"):
		z2[17] = z2[17] + 1
	if(string2[i2] == "S"):
		z2[18] = z2[18] + 1
	if(string2[i2] == "T"):
		z2[19] = z2[19] + 1
	if(string2[i2] == "U"):
		z2[20] = z2[20] + 1
	if(string2[i2] == "V"):
		z2[21] = z2[21] + 1
	if(string2[i2] == "W"):
		z2[22] = z2[22] + 1
	if(string2[i2] == "X"):
		z2[23] = z2[23] + 1
	if(string2[i2] == "Y"):
		z2[24] = z2[24] + 1
	if(string2[i2] == "Z"):
		z2[25] = z2[25] + 1
	i2 = i2 + 1
z = z - z2
print(z)
if(sum(z) == 0):
	print(1)
else:
	print(0)
