from numpy import *
string = input("digite o numero: ")
copy = ""
if(len(string) == 1):
	if(string[-1] == "0"):
		copy = copy  + "Zero"
	if(string[-1] == "1"):
		copy = copy  + "Um"
	if(string[-1] == "2"):
		copy = copy  + "Dois"
	if(string[-1] == "3"):
		copy = copy  + "Treis"
	if(string[-1] == "4"):
		copy = copy  + "Quatro"
	if(string[-1] == "5"):
		copy = copy  + "Cinco"
	if(string[-1] == "6"):
		copy = copy  + "Seis"
	if(string[-1] == "7"):
		copy = copy  + "Sete"
	if(string[-1] == "8"):
		copy = copy  + "Oito"
	if(string[-1] == "9"):
		copy = copy  + "Nove"
else:	
	if(string[-1] == "0" and string[-2] == "1"):
		copy = copy  + "Dez"
	if(string[-1] == "1" and string[-2] == "1"):
		copy = copy  + "Onze"
	if(string[-1] == "2" and string[-2] == "1"):
		copy = copy  + "Doze"
	if(string[-1] == "3" and string[-2] == "1"):
		copy = copy  + "Treze"
	if(string[-1] == "4" and string[-2] == "1"):
		copy = copy  + "Quatorze"
	if(string[-1] == "5" and string[-2] == "1"):
		copy = copy  + "Quinze"
	if(string[-1] == "6" and string[-2] == "1"):
		copy = copy  + "Dezesseis"
	if(string[-1] == "7" and string[-2] == "1"):
		copy = copy  + "Dezessete"
	if(string[-1] == "8" and string[-2] == "1"):
		copy = copy  + "Dezoito"
	if(string[-1] == "9" and string[-2] == "1"):
		copy = copy  + "Dezenove"
	if(string[-1] == "9","8","7","6","5","4","3","2","1","0" and string[-2] == "2"):
		copy = copy + "Vinte"
		if(string[-1] == "0"):
			copy = copy  + ""
		if(string[-1] == "1"):
			copy = copy  + " e Um"
		if(string[-1] == "2"):
			copy = copy  + " e Dois"
		if(string[-1] == "3"):
			copy = copy  + " e Treis"
		if(string[-1] == "4"):
			copy = copy  + " e Quatro"
		if(string[-1] == "5"):
			copy = copy  + " e Cinco"
		if(string[-1] == "6"):
			copy = copy  + " e Seis"
		if(string[-1] == "7"):
			copy = copy  + " e Sete"
		if(string[-1] == "8"):
			copy = copy  + " e Oito"
		if(string[-1] == "9"):
			copy = copy  + " e Nove"
	if(string[-1] == "9","8","7","6","5","4","3","2","1","0" and string[-2] == "3"):
		copy = copy + "Trinta"
		if(string[-1] == "0"):
			copy = copy  + ""
		if(string[-1] == "1"):
			copy = copy  + " e Um"
		if(string[-1] == "2"):
			copy = copy  + " e Dois"
		if(string[-1] == "3"):
			copy = copy  + " e Treis"
		if(string[-1] == "4"):
			copy = copy  + " e Quatro"
		if(string[-1] == "5"):
			copy = copy  + " e Cinco"
		if(string[-1] == "6"):
			copy = copy  + " e Seis"
		if(string[-1] == "7"):
			copy = copy  + " e Sete"
		if(string[-1] == "8"):
			copy = copy  + " e Oito"
		if(string[-1] == "9"):
			copy = copy  + " e Nove"
	if(string[-1] == "9","8","7","6","5","4","3","2","1","0" and string[-2] == "4"):
		copy = copy + "Quarenta"
		if(string[-1] == "0"):
			copy = copy  + ""
		if(string[-1] == "1"):
			copy = copy  + " e Um"
		if(string[-1] == "2"):
			copy = copy  + " e Dois"
		if(string[-1] == "3"):
			copy = copy  + " e Treis"
		if(string[-1] == "4"):
			copy = copy  + " e Quatro"
		if(string[-1] == "5"):
			copy = copy  + " e Cinco"
		if(string[-1] == "6"):
			copy = copy  + " e Seis"
		if(string[-1] == "7"):
			copy = copy  + " e Sete"
		if(string[-1] == "8"):
			copy = copy  + " e Oito"
		if(string[-1] == "9"):
			copy = copy  + " e Nove"
	if(string[-1] == "9","8","7","6","5","4","3","2","1","0" and string[-2] == "5"):
		copy = copy + "Cinquenta"
		if(string[-1] == "0"):
			copy = copy  + ""
		if(string[-1] == "1"):
			copy = copy  + " e Um"
		if(string[-1] == "2"):
			copy = copy  + " e Dois"
		if(string[-1] == "3"):
			copy = copy  + " e Treis"
		if(string[-1] == "4"):
			copy = copy  + " e Quatro"
		if(string[-1] == "5"):
			copy = copy  + " e Cinco"
		if(string[-1] == "6"):
			copy = copy  + " e Seis"
		if(string[-1] == "7"):
			copy = copy  + " e Sete"
		if(string[-1] == "8"):
			copy = copy  + " e Oito"
		if(string[-1] == "9"):
			copy = copy  + " e Nove"
	if(string[-1] == "9","8","7","6","5","4","3","2","1","0" and string[-2] == "6"):
		copy = copy + "Sessenta"
		if(string[-1] == "0"):
			copy = copy  + ""
		if(string[-1] == "1"):
			copy = copy  + " e Um"
		if(string[-1] == "2"):
			copy = copy  + " e Dois"
		if(string[-1] == "3"):
			copy = copy  + " e Treis"
		if(string[-1] == "4"):
			copy = copy  + " e Quatro"
		if(string[-1] == "5"):
			copy = copy  + " e Cinco"
		if(string[-1] == "6"):
			copy = copy  + " e Seis"
		if(string[-1] == "7"):
			copy = copy  + " e Sete"
		if(string[-1] == "8"):
			copy = copy  + " e Oito"
		if(string[-1] == "9"):
			copy = copy  + " e Nove"
	if(string[-1] == "9","8","7","6","5","4","3","2","1","0" and string[-2] == "7"):
		copy = copy + "Setenta"
		if(string[-1] == "0"):
			copy = copy  + ""
		if(string[-1] == "1"):
			copy = copy  + " e Um"
		if(string[-1] == "2"):
			copy = copy  + " e Dois"
		if(string[-1] == "3"):
			copy = copy  + " e Treis"
		if(string[-1] == "4"):
			copy = copy  + " e Quatro"
		if(string[-1] == "5"):
			copy = copy  + " e Cinco"
		if(string[-1] == "6"):
			copy = copy  + " e Seis"
		if(string[-1] == "7"):
			copy = copy  + " e Sete"
		if(string[-1] == "8"):
			copy = copy  + " e Oito"
		if(string[-1] == "9"):
			copy = copy  + " e Nove"
	if(string[-1] == "9","8","7","6","5","4","3","2","1","0" and string[-2] == "8"):
		copy = copy + "Oitenta"
		if(string[-1] == "0"):
			copy = copy  + ""
		if(string[-1] == "1"):
			copy = copy  + " e Um"
		if(string[-1] == "2"):
			copy = copy  + " e Dois"
		if(string[-1] == "3"):
			copy = copy  + " e Treis"
		if(string[-1] == "4"):
			copy = copy  + " e Quatro"
		if(string[-1] == "5"):
			copy = copy  + " e Cinco"
		if(string[-1] == "6"):
			copy = copy  + " e Seis"
		if(string[-1] == "7"):
			copy = copy  + " e Sete"
		if(string[-1] == "8"):
			copy = copy  + " e Oito"
		if(string[-1] == "9"):
			copy = copy  + " e Nove"
	if(string[-1] == "9","8","7","6","5","4","3","2","1","0" and string[-2] == "9"):
		copy = copy + "Noventa"
		if(string[-1] == "0"):
			copy = copy  + ""
		if(string[-1] == "1"):
			copy = copy  + " e Um"
		if(string[-1] == "2"):
			copy = copy  + " e Dois"
		if(string[-1] == "3"):
			copy = copy  + " e Treis"
		if(string[-1] == "4"):
			copy = copy  + " e Quatro"
		if(string[-1] == "5"):
			copy = copy  + " e Cinco"
		if(string[-1] == "6"):
			copy = copy  + " e Seis"
		if(string[-1] == "7"):
			copy = copy  + " e Sete"
		if(string[-1] == "8"):
			copy = copy  + " e Oito"
		if(string[-1] == "9"):
			copy = copy  + " e Nove"
print(copy)