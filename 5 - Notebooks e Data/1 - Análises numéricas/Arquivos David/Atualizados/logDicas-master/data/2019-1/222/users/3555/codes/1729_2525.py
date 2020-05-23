i=int(input())
j=i
dd = 0
while(j != 0):
 d = int(i/j)
 if( (i%j) == 0):
		 print(d)
		 dd = dd + 1
 j = j - 1
print(dd,"divisores")