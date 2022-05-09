from email.mime.nonmultipart import MIMENonMultipart
from http import server
import imp
from urllib import response
import requests #http requests

from bs4 import BeautifulSoup # web scraping

#send the email
import smtplib

#email body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


#system date and time manipulation
import datetime

now = datetime.datetime.now()

#email content placeholder

content = ''

#extracting hacker news Stories

def extract_news(url):
    print('Extracting Hacker News Stories...')
    cnt=''
    cnt+=('<b>HN Top Stories:</b>\n'+'-'*50+'<br>')
    response=requests.get(url)
    content=response.content
    soup=BeautifulSoup(content,'html.parser')
    for i,tag in enumerate(soup.find_all('td', attrs={'class':'title','valign':''})):
        cnt+=((str(i+1)+' :: ' +tag.text + "\n" + '<br>') if tag.text!='More' else '')
        print (tag.prettify)
    return (cnt)

ctn= extract_news('https://news.ycombinator.com/')
content+=ctn
content+=   ('<br>---------</br>')
content+=('<br><br>End of Message')

#print(content)

#lets send the email
print('Composing Email...')

#update your email details

SERVER = 'smtp.gmail.com' #'your smtp server'
PORT=587
FROM= 'tranvanxuan96haui@gmail.com'
TO='to'
PASS='yourpassword'


msg=MIMEMultipart()
msg['Subject'] = 'Top News Stories HN [Automated Email]' + ' ' + str(now.day) + '-' + str(now.year)

msg['From'] = FROM
msg['To'] = TO
msg.attach(MIMEText(content,'html'))

#fp.close()

print('Initiating Sever...')
server=smtplib.SMTP(SERVER,PORT)

server.set_debuglevel(1)

server.ehlo()
server.starttls()

server.login(FROM,PASS)
server.sendmail(FROM, TO, msg.as_string())
print('Email Sent...')

server.quit()
