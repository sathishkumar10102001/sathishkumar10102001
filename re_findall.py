import re
result=re.findall(r'am','hi am in tamils am in indian')
if result:
    print(result)
else:
    print("did not match")
#***************************************

import re
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
emails = re.findall(r'[\w\.-]+@[\w\.-]+', str) 
for email in emails:
 print(email)
 print(email)    
    
