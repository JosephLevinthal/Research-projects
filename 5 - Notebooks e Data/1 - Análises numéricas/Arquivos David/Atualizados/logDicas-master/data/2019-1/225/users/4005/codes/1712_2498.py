numa = int(input("numero de habitantes A: "))
numb = int(input("numero de habitantes B: "))
pa = float(input("percentual A: "))
pb = float(input("percentual B: "))
pa=pa/100
pb=pb/100
cont=0
while(numa < numb):
	numb=numb*pb+numb
	numa=numa*pa+numa
	cont+=1
print(cont)