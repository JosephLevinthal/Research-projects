numa= int(input("Numero de habitantes de uma cidade A"))
numb= int(input("Numero de habitantes de uma cidade B"))
pa=float(input("Percentual de crescimento populacional da cidade A"))
pb=float(input("Percentual de crescimento populacional da cidade B"))
a=0
pac=pa/100
pbc=pb/100
while(numa<numb and pac>pbc):
	numa=numa+(numa*pac)
	numb=numb+(numb*pbc)
	a=a+1
print(a)


