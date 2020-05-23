from numpy import*
x= array (eval (input("Digite as medias finais: ")))
h=0
while(size (x) >1) :
	h=0
	for i in x:
		if(i>= 5) and (i<7) :
			h=h+1
	print(h)
	x=array(eval(input(" Digite as medias: ")))