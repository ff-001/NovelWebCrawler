import requests
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
basedurl = 'http://novelfull.com'
url='http://novelfull.com/index.php/hidden-marriage.html?page=1&per-page=50'
#url = 'https://www.kanunu8.com/book4/10509/'
txt=requests.get(url).content
m1=re.compile(r'<span class="glyphicon glyphicon-certificate"></span>(.+)<span')
#print(m1.findall(txt))

raw = m1.findall(txt) 
m2 = re.compile(r'<a href="(.+)" title="(.+)">')
m3=re.compile(r'<p>(.+)</p>',re.S)  
m4=re.compile(r'<br />')          
m5=re.compile(r'&nbsp;&nbsp;&nbsp;&nbsp;')
chapter = []
with open('HW.txt','a') as f:
	for i in raw:	
		item = m2.findall(i)
		i_url=basedurl+item[0][0]  
        print(i_url)   
        r_nr=requests.get(i_url).content
        n_nr=m3.findall(r_nr)
        #print(n_nr)
        n=m4.sub('',n_nr[0]) 
        n2=m5.sub('',n)
        f.write('\n'+item[0][1]+'\n') 
        f.write(n2)
