n = float(input("Digite: "))

somap=0
contp=0
somai=0
conti=0
while(n!=0):
	if(n%2==0):
		somap=somap+n
		contp=contp+1
	else:
		somai=somai+n
		conti=conti+1
	n = float(input("Digite:"))	

if(somap==0.0):	
   print(0.0)
else:
	print(round(somap/contp,2))

if(somai==0.0):
	print(0.0)
else:
	print(round(somai/conti,2))