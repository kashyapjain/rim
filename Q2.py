import requests
import re
from bs4 import BeautifulSoup

url = input("Enter website : ")
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')

tel_pattern = r'tel:.*'
facebook_pattern = r'https://www.facebook.com/.*'
linkedin_pattern = r'.*linkedin.*'
email_pattern = r'(mailto:|).*(support|feedback).*'

for link in soup.find_all('a'):
    str = link.get('href')

    tel = re.match(tel_pattern, str)
    if(tel != None):
        print("Contact :")
        print(tel.group(0)[4:])
        continue

    facebook = re.match(facebook_pattern, str)
    if(facebook != None):
        print("Facebook :")
        print(facebook.group(0))
        continue

    linkedin = re.match(linkedin_pattern, str)
    if(linkedin != None):
        print("Linkedin :")
        print(linkedin.group(0))
        continue

    email = re.match(email_pattern, str)
    if(email != None):
        print("Email :")
        print(email.group(0)[7:])
        continue
