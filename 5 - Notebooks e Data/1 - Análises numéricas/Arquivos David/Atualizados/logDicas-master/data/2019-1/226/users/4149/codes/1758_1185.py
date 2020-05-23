from numpy import*
glic=array(eval(input("entre com o vetor:")))

quant=0
i=0
while(i < size(glic)):
	if (glic[i]>99):
		print(i)
		quant=quant+1
	i=i+1
print(quant)
	