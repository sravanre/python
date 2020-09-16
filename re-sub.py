# Regular Expressions - Substitution

import re

print(re.sub(r'\sAND\s', ' & ', 'A and B And C', flags=re.IGNORECASE))

text="My mobile is 9885970033. My atm pin in 3487"

print( re.sub(r'\d','*',text))
print( re.sub(r'\d+','*',text))
print( re.sub(r'0?[7-9]\d{9}','*',text))
