from numpy import*

x = input("string:")

conta = 0 
conte = 0
conti = 0
conto = 0
contu = 0

for ch in range(len(x)):
	if(x[ch]  == "a"):
		conta = conta + 1
	elif(x[ch] == "e"):
		conte = conte + 1
	elif(x[ch] == "i"):
		conti = conti + 1
	elif(x[ch] == "o"):
		conto = conto + 1
	elif(x[ch] == "u"):
		contu = contu + 1
		
print("a:",conta)
print("e:",conte)
print("i:",conti)
print("o:",conto)
print("u:",contu)

	


