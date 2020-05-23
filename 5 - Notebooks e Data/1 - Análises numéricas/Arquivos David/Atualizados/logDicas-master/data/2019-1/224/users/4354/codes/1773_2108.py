from numpy import *
string = input("digite a string: ")
copy = ""
i = 0
while(i<len(string)):
	if(string[i]=="A"):
		copy = copy + string[i]
	elif(string[i]=="E"):
		copy = copy + string[i]
	elif(string[i]=="I"):
		copy = copy + string[i]
	elif(string[i]=="O"):
		copy = copy + string[i]
	elif(string[i]=="U"):
		copy = copy + string[i]
	elif(string[i]=="a"):
		copy = copy + string[i]
	elif(string[i]=="e"):
		copy = copy + string[i]
	elif(string[i]=="i"):
		copy = copy + string[i]
	elif(string[i]=="o"):
		copy = copy + string[i]
	elif(string[i]=="u"):
		copy = copy + string[i]
	elif(string[i] == " "):
		copy = copy + " "
	else:
		copy = copy + "p"
	i = i + 1
print(copy)
