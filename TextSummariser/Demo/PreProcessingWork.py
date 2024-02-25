import re

def preProcess(a):
    a=re.sub("�","'",a)
    a=re.sub("'",'',a)
    a=re.sub("/",' or ',a)
    a=re.sub('�','"',a)
    a=re.sub('�','"',a)
    a=re.sub('"',' ',a)
    a=re.sub("p.m",'pm',a)
    return a



a=input("Enter the Text:")
a=preProcess(a)
print (a)
