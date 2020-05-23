ate20 = ['',' um',' dois',' tres',' quatro',' cinco',' seis',' sete',' oito',' nove',' dez',' onze',' doze',' treze',' quatorze',' quinze',' dezesseis',' dezesete',' dezoito',' dezenove']
dez = ['','',' vinte',' trinta',' quarenta',' cinquenta',' sessenta',' setenta',' oitenta',' noventa']
cem = ['',' cento',' duzentos',' trezentos',' quatrocentos',' quinhentos',' seissentos',' setecentos',' oitocentos',' novecentos']
mil =['',' mil',' dois mil',' tres mil',' quatro mil',' cinco mil',' seis mil',' sete mil',' oito mil',' nove mil',' dez mil']
string = '0000'+input("")
if(string[-2]=='1'):
	acu = (mil[int(string[-4])+int(string[-5])*10]+cem[int(string[-3])]+ate20[int(string[-2])*10+int(string[-1])])
else:
	acu = (mil[int(string[-4])+int(string[-5])*10]+cem[int(string[-3])]+dez[int(string[-2])]+ate20[int(string[-1])])
acu =  acu[1::]
if(acu==''):
	acu = 'zero'
elif(string[len(string)-3::]=="100"):
	acu = acu.replace("cento","cem")
acu = acu.replace(" "," e ")
acu = acu.replace(" e mil"," mil")
print(acu)