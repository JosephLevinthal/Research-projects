escala = input("Digite a escala: (C/F)")
temp = float(input("Temperatura"))
tf = (1.8*temp)+32
tc = (temp-32)/1.8
if(escala == "C"):
	print (round(tf,2))
else:
	print(round(tc,2))