a =  float(input())
b =  float(input()) 
c =  float(input())   
d =  float(input())   
e =  float(input())   
f =  float(input())   
# processamento de x

cimax = c*e - b*f 
baixox = a*e - b*d
if( baixox == 0 ):
  print("Nao tem solucao")
else:
  x = cimax / baixox

#processamento de y

cimay = a*f - c*d
baixoy = a*e - b*d
if(baixox !=0 ):
	y = cimay / baixoy
	
if( baixox!=0 ):
	print(x)
	print(y)

