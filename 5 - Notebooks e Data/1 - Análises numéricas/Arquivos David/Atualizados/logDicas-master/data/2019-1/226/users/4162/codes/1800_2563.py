from numpy import*
me= array(eval(input("insira as medias dos alunos: ")))

while size(me)!=1:
	ap=0
	for l in me:
		if l>=5 and l<7:
			ap=ap+1
	print(ap)
	me= array(eval(input("insira as medias dos alunos: ")))

