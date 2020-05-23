s = input("string inicial:")
s1 = s.replace(" " , "")

inv = "" #inversa
i = -1

while(i >= -len(s)):
	inv = inv + s[i]
	i = i - 1
print(s1.upper())
if(inv==s):
	print(1)
else:
	print(0)