cek = float(input("Consumo de energia em kWh: "))
instal = input("Tipo de instalacao: ").upper()
print("Entradas: ",cek ,"kWh" ,"e tipo" ,instal)

#R = residencial   #I = industrial   #C = comercial

if((cek <= 500) and (instal == "R")):
	vt = (cek * 0.44) 
	print("Valor total: " , vt)
elif((cek > 500) and (instal == "R")):
	vt = (cek * 0.65)
	print("Valor total: " , vt)
elif((cek <= 1000) and (instal == "C")):
	vt = (cek * 0.55) 
	print("Valor total: " , vt)
elif((cek > 1000) and (instal == "C")):
	vt = (cek * 0.60)
	print("Valor total: ", vt)
elif((cek <= 5000) and (instal == "I")):
	vt = (cek * 0.55) 
	print("Valor total: " , vt)
elif((cek > 5000) and (instal == "I")):
	vt = (cek * 0.60)
	print("Valor total: " , vt)
else:
	print("Dados invalidos")
