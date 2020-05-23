s = input()

r = t = ""

for i in s:
	if(i == "a"):
		r = s.replace("a", "")
		rt = 0
		for i in r:
			if(i == "A"):
				t = r.replace("A", "")
				rt = 1
	elif(i == "A"):
		r = s.replace("A", "")
		rt = 0
		for i in r:
			if(i == "a"):
				t = r.replace("a", "")
				rt = 1

if(rt == 0):
	print(r)
else:
	print(t)