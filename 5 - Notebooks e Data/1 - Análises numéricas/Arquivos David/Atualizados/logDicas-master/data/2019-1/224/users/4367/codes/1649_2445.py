x= input("escolha C ou F")
if (x.upper())=="C":
	C=float(input("escolha a temperatura"))
	C=(C*9/5)+32
	print(round(C, 2))

else:
	F= float(input("escolha a temperatura"))
	F=(F-32)*5/9
	print(round(F, 2))
