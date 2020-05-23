from numpy import*

s = input()

s1 = array([], dtype = str)

i = 0
j = 0
while(i < len(s)):
	if(i % 3 == 0 and i != 0):
		s1 = append(s1, [s[i-3:i] + "."])
		j = i
	i = i + 1
	
s1 = append(s1, [s[j:]])

s = ""
i = 0
while(i < size(s1)):
	s = s + s1[i]
	i = i + 1

print(ssob)