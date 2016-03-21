import string
str0 = 'abc'
str1 = 'ABC'
t = string.maketrans(str0, str1)
a = 'abc123'.translate(t,'123')
print a
