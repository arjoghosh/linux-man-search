import requests
from bs4 import BeautifulSoup
x=input("Enter command name : ")
x=x.strip()
x=x.lower()
r = requests.get("http://man.he.net/?topic="+x+"&section=all")
html=r.content
bsObj = BeautifulSoup(html,"html.parser")
bsObj = bsObj.select('pre')
for link in bsObj:
    s=link.get_text()
    if 'SEE ALSO' in s:
        s = s[:s.index('SEE ALSO')]
    elif 'ORIGINAL AUTHORS' in s:
        s = s[:s.index('ORIGINAL AUTHORS')]
    elif 'CURRENT AUTHORS' in s:
        s = s[:s.index('CURRENT AUTHORS')]
    elif 'AUTHORS' in s:
        s = s[:s.index('AUTHORS')]
    elif 'NOTES' in s:
        s = s[:s.index('NOTES')]
    for i in range(0,9):
        s=s.replace('('+str(i)+')','')
    print(s)
