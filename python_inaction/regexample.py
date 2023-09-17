b = "Hello" in "hello world".lower()
print(b)


txt = "My phone number is 123-123-1234. Please call me to this phone number"
import re

pattern = 'number'
matched = re.search(pattern, txt)
print(matched)

print(matched.span())
print(matched.start())
print(matched.end())

matched = re.findall(pattern, txt)
print(matched)
print(len(matched))

for m in re.finditer(pattern, txt):
    print(m.span())

# identifier
# \d = any number
# \D = anything but a number
# \s = space
# \S = anything but a space
# \w = any letter
# \W = anything but a letter

# phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d', txt)
phone = re.search(r'\d{3}-\d{3}-\d{4}', txt)
print(phone)
print(phone.group())

###### Quantifiers ######
# *	Asterisk	Match its preceding element zero or more times.
# +	Plus	Match its preceding element one or more times.
# ?	Question Mark	Match its preceding element zero or one time.
# { n }	Curly Braces	Match its preceding element exactly n times.
# { n ,}	Curly Braces	Match its preceding element at least n times.
# { n , m }	Curly Braces	Match its preceding element from n to m times.

import re

txt = "My phone number is 123-123-1234. Please call me to this phone number"

phone = re.search(r'\d{3}-\d*-\d{3,}', txt)
print(phone)
print(phone.group())

# detail with group
pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
output = re.search(pattern, txt)
# index starts from 1
print(output.group(3))


import re
r = re.search(r'cat|dog', 'cats and dogs')
print(r)

r = re.findall(r'.at', 'The person wearing the hat sat in the shade')
print(r)

r = re.findall(r'^\d', '1 person wearing the hat sat in the shade2')
print(r)

r = re.findall(r'[^!.?]+', "Jesus! Hello World. Typical?")
print(" ".join(r))

r = re.findall(r'[\w]+-[\w]+', "Here is hypen-string")
print(r)

r = re.findall(r' (cat|sat|hat)', "person holding a cat sat wearing at hat")
print(r)