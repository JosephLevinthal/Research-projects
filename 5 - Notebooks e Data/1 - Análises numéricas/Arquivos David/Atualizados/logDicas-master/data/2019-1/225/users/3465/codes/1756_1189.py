string = input("")
string = string.replace(" ","")
print(string.upper())
if(string[::-1]==string):
	print(1)
else:
	print(0)