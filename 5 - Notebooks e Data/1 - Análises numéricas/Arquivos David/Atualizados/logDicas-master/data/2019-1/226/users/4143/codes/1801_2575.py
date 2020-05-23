from numpy import*
a =input("ata: ").upper()
b = zeros(3,dtype=int)
c=len(a)
i = 0 
tv=0
net=0
you=0
for x in c :
	if (x[i] == "TV"):
		tv+=1
	elif(x[i]=="NETFLIX"):
		net+=1
	elif(x[i]=="YOUTUBE"):
		you+=1
	i+=1
b[0]=tv
b[1]=net
b[2]=you
print(b)