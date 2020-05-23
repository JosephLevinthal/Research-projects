tempo=int(input("escreva: "))

if(tempo<=200):
	total=5000+(100*tempo)
if(tempo>200):
	total=8000+(100*200)+90*(tempo-200)
print(round(total))