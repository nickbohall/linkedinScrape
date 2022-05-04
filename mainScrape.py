from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.linkedin.com/jobs/search/?f_E=2%2C3&f_JT=F&f_WT=2&keywords=data%20scientist').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('div', class_='application-outlet')
print(html_text)
