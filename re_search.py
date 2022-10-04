import re
result=re.search(r'tamil','am in tamil')
if result:
    print(result.group())
else:
    print("did not match")


#*******************************************

import re
str='an example word:cat!!'
match=re.search(r' exa\w\w\w\w',str)

if match:
    print('found',match.group())
else:
    print('did not find')

#********************************************

str='purple alice-b@google.com monkey dishwasher'
match=re.search(r'\w+@\w+',str)
if match:
    print(match.group())
    
#********************************************
str = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'([\w.-]+)@([\w.-]+)', str)
if match:
    print(match.group())
    print(match.group(1))
    print(match.group(2))
    
