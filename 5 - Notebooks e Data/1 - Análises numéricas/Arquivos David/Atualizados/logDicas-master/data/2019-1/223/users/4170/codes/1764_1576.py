from numpy import*
ve =  array(eval(input("Vetor 1: ")))
vb =  array(eval(input("Vetor 2: ")))
i = 0
e = 0
b = 0
while i < size(ve) and i < size(vb):
	if(ve[i] == 11 and vb[i]== 11):
		e = e + 1
		b = b + 1
	elif(ve[i] == 11 and vb[i] == 22):
		b = b + 1
	elif(ve[i] == 11 and vb[i] == 33):
		e = e + 1
	elif(ve[i] == 22 and vb[i] == 22):
		e = e + 1
		b = b + 1
	elif(ve[i] == 22 and vb[i] == 11):
		e = e + 1 
	elif(ve[i] == 22 and vb[i] == 33):
		b = b + 1
	elif(ve[i] == 33 and vb[i] == 33):
		e = e + 1
		b = b + 1
	elif(ve[i] == 33 and vb[i] == 11):
		b = b + 1
	elif(ve[i] == 33 and vb[i] == 22):
		e = e + 1
	i = i + 1		
print(i)
if(e > b):
	print("EUSAPIA")
elif(b > e):
	print("BARSANULFO")
else:
	print("EMPATE")