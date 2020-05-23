from numpy import*
mf = array(eval(input("digite as medias finais dos alunos: ")))
while (size(mf)>1):
	ap = 0
	for elemento in mf:
		if elemento >= 5 and elemento < 7:
			ap = ap + 1
	print(ap)
	mf = array(eval(input("digite as medias finais dos alunos: ")))

