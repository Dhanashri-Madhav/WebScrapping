

from http import server


import mimetypes
from xmlrpc.client import SERVER_ERROR
import requests

from bs4 import BeautifulSoup

import smtplib

from email.mime.multipart import MIMEMultipart

from email.mime.text import MIMEText

import datetime

now = datetime.datetime.now()

content = ""

def extract_data(url):
    print("extracting data")
    cnt= ""
    cnt+=('<b>Top news:</b>\n'+'<br>'+'-'*80+'</br>')
    response = requests.get(url)
    print("response: ",response)
    content = response.content
    print("content: ",content)
    soup = BeautifulSoup(content,'html.parser')
    print('soup:  ', soup)
    for i, tag in enumerate(soup.find_all('td',attrs={'class':'title','valign': ""})):
        print('tag: ', tag)
        print('tg.text', tag.text)
        cnt+=((str(i+1)+'::'+tag.text+ "\n"+'</br>') if tag.text!=  'More' else "")
        print('cnt: ', cnt)
    return(cnt)


cnt = extract_data("https://news.ycombinator.com/")
content += cnt
content += ('<br>---------------------</br>')
content += ('<br> Thanks and regards</br>')

print('composing Emails')

SERVER = 'smtp.navgurukul.org'
PORT = 3000
FROM = "dhanashri20@navgurukul.org"
TO = "odhanashri@gmail.com"
PASS = 'dhannooo'

msg = MIMEMultipart()

msg['Subject'] = 'TOP NEWS from HV rank[Automated email]'+ ' '+ str(now.day)+ "-"+ str(now.month)+ "-"+ str(now.year)

msg['From']= FROM
msg['To']= TO
msg.attach(MIMEText(content, 'html'))

print('initiating server')

server = smtplib.SMTP(SERVER,PORT)
server.set_debuglevel(1)
print('1')
print('2')
server.starttls
print('3')
server.login(FROM, PASS)
print('4')
server.sendmail(FROM, TO, msg.as_string())
print('5')

print('email sent')

server.quit
