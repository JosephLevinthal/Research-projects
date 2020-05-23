n=input("C/F")
t=int(input("valor da temperatura:"))

C=(5/9)*(t-32)

F=(1.8*t)+32

if(n=="C"):
	print(round(F,2))
	
else:
	print(round(C,2))