from numpy import*
s = input("s: ")
k = ""
i = 0
while(i<len(s)):
	if(s[i] != ""):
		k = k + s[i]
	i = i + 1
print(k.upper())

j = ""
i = -1
while(i >= -len(s)):
	if(s[i] != ""):
		j = j + s[i]
	i = i - 1
n = 0
if(j == k):
	n = n + 1
print(n)