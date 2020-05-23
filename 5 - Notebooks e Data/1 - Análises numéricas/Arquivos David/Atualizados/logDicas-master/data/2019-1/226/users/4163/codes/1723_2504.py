qvirus=int(input("quantidade inicial do virus: "))
qleu=int(input("quantidade inicial de leucocitos "))
pvirus = int(input("percentual diaria do virus: "))
pleuco= int(input("multiplicacao diaria de leucocitos: "))

a = pvirus / 100
b = pleuco /100

dias = 0


while(qvirus * 2  >(qleu)):
	qvirus = qvirus+(qvirus*a)
	qleu = qleu+(qleu*b)
	dias = dias + 1
	
print(dias)
	