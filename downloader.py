import requests
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
url='https://www.kanunu8.com/book4/10509/'
txt=requests.get(url).content.decode('gbk') 
m1=re.compile(r'<td colspan="4" align="center"><strong>(.+)</strong>')
#print(m1.findall(txt))
m2=re.compile(r'<td( width="25%")?><a href="(.+\.html)">(.+)</a></td>')
#print(m2.findall(txt))
raw=m2.findall(txt) 
sanguo=[]
for i in raw:
    sanguo.append([i[2],url+i[1]]) 

#print(sanguo)

m3=re.compile(r'<p>(.+)</p>',re.S)  
m4=re.compile(r'<br />')          
m5=re.compile(r'&nbsp;&nbsp;&nbsp;&nbsp;')
with open('HW.txt','a') as f:
    for i in sanguo:
        i_url=i[1]  
        print("download----->",i[0])   
        r_nr=requests.get(i_url).content.decode('gbk')
        n_nr=m3.findall(r_nr)
        #print(n_nr)
        n=m4.sub('',n_nr[0]) 
        n2=m5.sub('',n)
        f.write('\n'+i[0]+'\n') 
        f.write(n2)
