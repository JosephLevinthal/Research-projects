i=int(input())
j=i
dd = 0
while(j != 1):
 d = int(i/j)
 if( (i%j) == 0):
		 print(d)
		 dd = dd + d
 j = j - 1
if(dd == i):
	print("PERFEITO")
else:
	print("NAO PERFEITO")