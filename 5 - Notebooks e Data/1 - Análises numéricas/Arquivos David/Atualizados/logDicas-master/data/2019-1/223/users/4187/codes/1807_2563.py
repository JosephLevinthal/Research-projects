from numpy import*
media_finais = array(eval(input("medias finais dos alunos matriculados:")))

while(size(media_finais) > 1):

	aprovados = 0
	
	for elemento in media_finais:
		if( 5 <= elemento < 7 ):
			aprovados = aprovados + 1
			
	print(aprovados)
	
	media_finais = array(eval(input("proximas medias:")))