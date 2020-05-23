hj=int(input("hj"))
da=int(input("da"))

#fututo=(hoje+dias)%7
ft=(hj+da)%7
	
	
if(hj>=0 and hj<7 and da>0):
	if(hj==0):	
		hj="domingo"
	if(hj==1):
		hj="segunda"
	if(hj==2):
		hj="terca"
	if(hj==3):
		hj="quarta"
	if(hj==4):
		hj="quinta"
	if(hj==5):
		hj="sexta"
	if(hj==6):
		hj="sabado"
		
	if(ft==0):
		ft="domingo"
		print("Hoje eh", hj, "e o dia futuro eh",ft)
	if(ft==1):
		ft="segunda"
		print("Hoje eh", hj, "e o dia futuro eh",ft)
	if(ft==2):
		ft="terca"
		print("Hoje eh", hj, "e o dia futuro eh",ft)
	if(ft==3):
		ft="quarta"
		print("Hoje eh", hj, "e o dia futuro eh",ft)
	if(ft==4):
		ft="quinta"
		print("Hoje eh", hj, "e o dia futuro eh",ft)
	if(ft==5):
		ft="sexta"
		print("Hoje eh", hj, "e o dia futuro eh",ft)
	if(ft==6):
		ft="sabado"
		print("Hoje eh", hj, "e o dia futuro eh",ft)
else:
	print("A entrada", hj ,"eh invalida")
	
		
		
		
		
		
		
		
		
		
	
	
	
	
	
	
	
	
	
	
	
	
	

