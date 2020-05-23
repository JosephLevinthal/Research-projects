m = int(input("m:"))
d = int(input("d:"))
mc=int(input("mc:"))
mr=int(input("mr:"))
mes=0
moed=m
while(moed>0):
	moed=moed+mc-d-mr
	mes=mes+1
print(mes)