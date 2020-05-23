from numpy import*
vet = array(eval(input("TV,NETFLIX ou YOUTUBE ?")))

TNY = zeros(3, dtype=int)
for i in range(size(vet)):
	vet[i] = vet[i].upper()
	if(vet[i] == "TV"):
		TNY[0] = TNY[0] + 1
	elif(vet[i] == "NETFLIX"):
		TNY[1] = TNY[1] + 1
	elif(vet[i] == "YOUTUBE"):
		TNY[2] = TNY[2] + 1
print(TNY)