s = input().upper()

r = s
i = 0
while(i < len(s)):
	if(s[i] == " "):
		r = s.replace(" ", "")
		break
	i = i + 1

print(r)
		
t = ""
j = len(r) - 1
while(j >= 0):
	t = t + r[j]
	j = j - 1

if(t == r):
	print(1)
else:
	print(0)