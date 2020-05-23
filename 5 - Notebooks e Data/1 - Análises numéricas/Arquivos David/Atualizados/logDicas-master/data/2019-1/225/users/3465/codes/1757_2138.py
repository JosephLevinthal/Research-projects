string = input("")
x=[string[i] for i in range(len(string)) if not(string[i] == 'a' or string[i] == 'e' or string[i] == 'i' or string[i] == 'o' or string[i] == 'u')]
print(''.join(x))