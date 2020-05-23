from numpy import*
v=array(eval(input("medias finais: ")))

while(size(v)>1):
	a=0
	for i in v:
		if(i>=5 and (i<7)):
			a=a+1
	#v=array(eval(input("medias finais: ")))
	print(a)
	v=array(eval(input("medias finais: ")))
		
