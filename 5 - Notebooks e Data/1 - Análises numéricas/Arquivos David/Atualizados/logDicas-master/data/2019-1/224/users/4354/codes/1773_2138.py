from numpy import *
string = input("digite a string: ")
copy = ""
i = 0
while(i<len(string)):
	if(string[i]=="A"):
		copy = copy + ""
	elif(string[i]=="E"):
		copy = copy + ""
	elif(string[i]=="I"):
		copy = copy + ""
	elif(string[i]=="O"):
		copy = copy + ""
	elif(string[i]=="U"):
		copy = copy + ""
	elif(string[i]=="a"):
		copy = copy + ""
	elif(string[i]=="e"):
		copy = copy + ""
	elif(string[i]=="i"):
		copy = copy + ""
	elif(string[i]=="o"):
		copy = copy + ""
	elif(string[i]=="u"):
		copy = copy + ""
	else:
		copy = copy + string[i]
	i = i + 1
print(copy)
