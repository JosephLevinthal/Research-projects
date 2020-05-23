p = int(input("posicao"))
if p==1:
	x = 25
elif p==2:
	x = 18
elif p==3:
	x = 12
elif p<0:
	x = 0
elif 3<p<=10:
	x = 14-p
else:
	x = 0
total = 0
while (p != 0):
		p = int(input("posicao"))
		total = total + x
print(total)