from numpy import*

media = array(eval(input("medias:")))

aprovados = 0

while size(media) > 1:
	aprovados = 0

	for elemento in media:
		if(  5 <= elemento < 7 ):
			aprovados = aprovados + 1
			
	print(aprovados)
	
	media = array(eval(input("medias:")))
	
			
