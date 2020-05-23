ti=float(input("q: "))
pc=float(input("p: "))
qa=float(input("w: "))

time=0

while(0<ti<12000):
	acres=ti*(pc/100)
	ti+=acres
	ti-=qa
	time+=1
if(ti<=0):
	print("EXTINCAO")
else:
	print("LIMITE")
print(time)