tmbq=int(input())
tcresc=float(input())
qvendida=int(input())
i=0
while(tmbq<=12000 and tmbq>0):
	soma=tmbq*(tcresc/100)
	tmbq=soma+tmbq-qvendida
	i=i+1
if(tmbq>12000 ):
	print("LIMITE")
	print(i)
if(tmbq<=0):
	print("EXTINCAO")
	print(i)
