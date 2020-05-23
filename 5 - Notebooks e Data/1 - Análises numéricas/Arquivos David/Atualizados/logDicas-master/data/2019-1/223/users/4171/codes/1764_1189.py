from numpy import *

s = input().upper()

print(s.replace(" ", ""))

if s[-1] == s[0]:
	print(1)
else:
	print(0)