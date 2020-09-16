#Regular expressions - findall

import re

#find any number anywhere in the string

print(re.findall("\d+","3 pens cost 20 rupees and 50 paise"))

#find any number at the begining of the string
print(re.findall("^\d+","3 pens cost 20 rupees and 50 paise"))

#find any number at the end of the string
print(re.findall("\d+$","3 pens cost 20 rupees and 50"))

