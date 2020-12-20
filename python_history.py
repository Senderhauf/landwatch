import requests
r = requests.get('https://www.landwatch.com/default.aspx?ct=r&type=5,62&r.PSIZ=5,100&pn=5000&px=20000')
import requests
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"
}
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"}
url = "https://www.landwatch.com/default.aspx?ct=r&type=5,62&r.PSIZ=5,100&pn=5000&px=20000"
r = requests.get(url, headers=headers)
r.status_code
r
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0", "X-Requested-With": "XMLHttpRequest"}
r = requests.get(url, headers=headers)
r
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0", "X-Requested-With": "XMLHttpRequest", "Cookie": "Cookie: .ASPXANONYMOUS=upe6FpeU1gEkAAAAZDRiOTQ3NzktMDY2Yy00YzVlLWEyMzItM2IxZTYyMTA1ZGJhlGYfKYwNe1LtI9oZsB_BvcAVPWk1; 1stref=https://www.google.com/:::https://www.landwatch.com/Help:::2020-07-19T19:45:50.876Z; mailmunch_second_pageview=true; _mailmunch_visitor_id=507159ec-7f05-4e7e-9a2d-c60f2d8abdf1; ak_bmsc=4C91F3E3A0EF65B793A2EEE5619FD6B0ACE82BA73B630000DE1D185F6AFB336A~plUmApq0sZKfsjln9pJRqR/CwQrsToVb4NqRYZol667QxexuU2BIg/Iq8syMkuA7koqz312lMsbU4vzmEzcHAtxDHaQ+0+PFkr05xDFgOzTweoCgvTnabGeJxdu3u1MpnLTpUTuO11PkX8n8JGxQFlvAfw+703i+W6gwImndm4NzvFluc4rSnY5Ch8cimFRUtQfraOZz5BtF++VnWMRvdPOKfBmbU9Z1xbkmKOoiPt9RE=; bm_sv=1137D2639351DF8695C26E09DC5A85AB~80v9I0YxbKIE7Hjnro6TfY4e+vHOgf18NeFlXQ9NsaB8Ilg1os625S18HmlJ9uSiTTT6F7yf2jXm4ywclXTB/EJX3RP3c511jbBUjGVe3ST2wtSQmr/xX2mCnEempvEy9Oga+U7Ndx5KxX1SWTG1A+B7swF4XtLFcWqwb4RYTMI=; bm_mi=3CC8E4122D70E54CD1213AA12CC021A0~i49vIZXv5lnbSHvaQkD3jPSzgORC91YCZmkUdeoHyS3EVCVVsPbXdd96x/WByLWICY7+EfGBdbyrV84eaeMaSX2q8OrlqCVPNZ4thX7ZS87emsf2gzkjUzUTL8YvNvyPex4kzEDQiP96r1xrTxMu+RkCmDcK/pgtngonoWYuPiH1+NenlCJktX75YQeaCaZ8572I/chwupDtH7eg25R2VDdykN1gQeDf0Hg08g67yr4="}
r
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"}
import requests
url = "https://www.landwatch.com/default.aspx?ct=r&type=5,62&r.PSIZ=5,100&pn=5000&px=20000"
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"}
r = requests.get(url, headers=headers)
r
r.text
from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())
import requests
from bs4 import BeautifulSoup
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"}
url = "https://www.landwatch.com/default.aspx?ct=r&type=5,62&r.PSIZ=5,100&pn=5000&px=20000"
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')
links = soup.find_all('p', {"data-action": "resultsTitle"})
links
links = soup.find_all('a', {"data-action": "resultsTitle"})
links
len(links)
links[0]
links[0].get_text()
inner_text = links[0].get_text()
inner_text
inner_text = links[0].get_text()
inner_text.index('Acres')
inner_text[(3+5)::]
inner_text[inner_text.index('Acres')::]
link[0]
links[0]
links[0].href
links[0]['href']
inner_text[inner_text.index('Acres')::]
inner_text[inner_text.index('\xao')::]
inner_text[inner_text.index('\\xao')::]
inner_text[inner_text.index('/\xao')::]
inner_text[inner_text.index('xao')::]
inner_text
inner_text[inner_text.index('xa0')::]
inner_text
inner_text.index('xa0')
inner_text.index(\xa0)
inner_text.index("\n")
inner_text.split("\n")
link[0].select('br').extract()
links[0].select('br').extract()
links[0].select('br')
links[0].prettify()
links[0].find('br')
links[0].find('br').extract()
links[0]
links[0].inner_text
links[0].get_text()
inner_text
inner_text.replace("\n", "")
inner_text[(inner_text.index('xa0')+11)::]
inner_text[(inner_text.index('Acres')+11)::]
inner_text[(inner_text.index('Acres')+12)::]
inner_text_sans_acres = inner_text[(inner_text.index('Acres')+12)::]
inner_text_sans_acres.split('$')
inner_text[(inner_text.index('Acres'))::]
inner_text[::(inner_text.index('Acres'))]
inner_text[::inner_text.index('Acres')]
inner_text
inner_text[inner_text.index('Acres')::]
inner_text[:inner_text.index('Acres')]
arr = ['a']
arr[1]
true 
True
True if len(arr) else False
len(arr) == True
len(arr) == False
states = ['NM', 'CO', 'CA']
'WI' in states
'WI' not in states
import psycopg2'
conn = psycopg2.connect("dbname=landAndFarm user=postgres password=postgres")
conn = psycopg2.connect(dbname="landAndFarm" user="postgres" password="postgres")
conn = psycopg2.connect(dbname="landAndFarm", user="postgres", password="postgres")
with open('../zip_code_database.csv') as csvfile:
i = 0
i += 1
i
i += 1
error = Error('this is an error')
try:
	raise Exception('aaaaaaaaaaaaaaaaaaa')
catch:
import sys
try:
	raise Exception('aaaaaaaaaaaaaaaaaa')
except:
try:
	raise Exception('aaaaaaaaaaaaaaaaaa')
except (Exception) as error:
	sys.exit(error)
d = date()
import date
import time
import datetime
from datetime import datetime, date
import calendar
timestamp = calendar.timgm(d.timetuple())
d = date()
datetime.now()
timestamp = datetime.timestamp(datetime.now())
timestamp
d = {'a': 1, 'b': 2}
d['a']
d
d['c
d['c']
try:
	e = d['c']
except (Exception) as error:
	print(error)
else:
	print('no error')
e
e = ''
try:
	e = d['c']
except (Exception) as error:
	print('error')
else:
	print('no error')
try d['c'
try d['c'] except KeyError print('error') else print('no error')
try: d['c'] except: KeyError print('error') else: print('no error')
from lxml.html import fromstring
import requests
from itertools import cycle
import traceback
url = 'https://hidemy.name/en/proxy-list/?country=US&type=s#list'
response = requests.get(url)
parser = fromstring(response.text)
proxies = set()
parser
parser.xpath('//tbody/tr')
response
response.text
    property_info['acres'],
      geometry,
      datetime.utcnow(),
      property_info['zip_code'],
   ]
   insert_cmd = 'INSERT INTO listings (%s) VALUES %s ON CONFLICT DO NOTHING'
   insertDB(insert_cmd, columns, values)
def insertZipCodeDB(csv_row):
   """ Insert zip code info into database """
   columns = ['zip_code', 'primary_city', 'state', 'county', 'latitude', 'longitude']
   values = [csv_row['zip'], csv_row['primary_city'], csv_row['state'], csv_row['county'], csv_row['latitude'], csv_row['longitude']]
   insert_cmd = 'INSERT INTO zip_codes (%s) VALUES %s ON CONFLICT DO NOTHING'
   insertDB(insert_cmd, columns, values)
def connectDB():
   """ Connect to the PostgreSQL database server and insert zip code info """
   try:
      # read connection parameters
      params = config()
      # connect to the PostgreSQL server
      global db_connection
      db_connection = psycopg2.connect(**params)
      # create a cursor
      global db_cursor
      db_cursor = db_connection.cursor()
   except (Exception, psycopg2.DatabaseError) as error:
      clean_up()
      sys.exit(error)
def useZip(row):
   return row['type'] == 'STANDARD' and row['state'] in STATES_LIST
def main():
   BASE_URL = 'https://www.landandfarm.com/search/'
   min_acre = 5
   max_acre = 100
   min_price = 5000
   max_price = 40000
headers = {'User-Agent': 'Mozilla/5.0 (X11: Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'}
response = requests.get(url, headers=headers)
response
response.text
parser.xpath('//tbody/tr')
parser = fromstring(response.text)
parser.xpath('//tbody/tr')
i = parser.xpath('//tbody/tr')[0]
i
i.xpath('.//td[0])
i.xpath('.//td[0]')
i.xpath('.//td[1]')
i.xpath('.//td[1]').inner_text
i.xpath('.//td[1]/text()')
i.xpath('.//td[1]/text()')[0]
i.xpath('.//td[2]/text()')[0]
from rotate-request-proxies import get_proxies
from rotate_request_proxies import get_proxies
proxies = get_proxies()
proxies
from rotate_request_proxies import get_proxies
get_proxies()
get_proxies()[1]
proxies = get_proxies()
next(proxies)
proxies.pop()
get_proxies().len()
len(get_proxies())
headers = {'User-Agent': 'Mozilla/5.0 (X11: Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'}
url = 'https://hidemy.name/en/proxy-list/?country=CAUS&maxtime=1500&type=s&anon=234#list'
response = request.get(url, headers=headers)
import requests
response = request.get(url, headers=headers)
response = requests.get(url, headers=headers)
response.text
from lxml.html import fromstring
parser = fromstring(response.text)
parser.xpath('//tbody/tr/td[1]/text()')
i =parser.xpath('//tbody/tr/')
i = parser.xpath('//tbody/tr')
i.xpath('.//td[1]/text()')
i = parser.xpath('//tbody/tr')
i
i = parser.xpath('//tbody/tr')[0]
i
i.xpath('.//td[1]/text()')
i.xpath('.//td[1]/text()')[0]
from rotate_request_proxies import get_proxies
get_proxies()
len(get_proxies())
i.xpath('.//td[1]/text()')[0]
i.xpath('.//td[2]/text()')[0]
from validate_ip import validIPAddress, validPortNumber
validIPAddress(ip_addr_
ip_addr = i.xpath('.//td[1]/text()')[0]
port = i.xpath('.//td[2]/text()')[0]
validIPAddress(ip_addr)
from validate_ip import validIPAddress, validPortNumber
validIPAddress(ip_addr)
from validate_ip import validIPAddress, validPortNumber
validIPAddress(ip_addr)
validIPAddress
from validate_ip import validIPAddress, validPortNumber
validIPAddress(ip_addr)
ip_addr
validIPAddress('')
from validate_ip import validIPAddress, validPortNumber
validIPAddress(ip_addr)
validIPAddress(IP-ip_addr)
validIPAddress(IP=ip_addr)
validIPAddress(ip_addr)
from validate_ip import validIPAddress, validPortNumber
validIPAddress(ip_addr)
from validate_ip import validIPAddress, validPortNumber
validIPAddress(ip_addr)
"IPv4" == True
"IPv4" == False
"IPv4" is True
"IPv4" == True
from validate_ip import validIPAddress, validPortNumber
validIPAddress(ip_addr)
from validate_ip import validIPAddress, validPortNumber
validIPAddress('1.1.1.1')
from rotate_request_proxies import get_proxies
get_proxies()
len(get_proxies())
from rotate_request_proxies import get_proxies
len(get_proxies())
from rotate_request_proxies import get_proxies
get_proxies()
from rotate_request_proxies import get_proxies
get_proxies()
from rotate_request_proxies import cycle_proxies
cycle_proxies(get_proxies())
from rotate_request_proxies import cycle_proxies, get_proxies
cycle_proxies(get_proxies())
import logging
logging.info('hello')
logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
logging.warning('hello')
logging.info('hello')
logging.warning('hello')
logging.error('hello')
logging.debug('hello')
logging.debug('debug')
import requests
url = 'https://www.landandfarm.com/search/VT/05001-land-for-sale/?MinAcreage=5&MaxAcreage=100&MinPrice=5000&MaxPrice=40000'
headers = {'User-Agent': 'Mozilla/5.0 (Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0'}
proxy = '173.192.128.238:25'
requests.get(url, headers=headers, proxies={"http": proxy, "https": proxy})
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
user-agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
user-agent
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
headers = {'User-Agent': user_agent}
requests.get(url, headers=headers, proxies={"http": proxy, "https": proxy})
requests.get(url, proxies={"http": proxy, "https": proxy})
requests.get(url, headers=headers)
from expressvpn.wrapper import random_connect
random_connect()
from expressvpn import disconnect
from expressvpn import connect
disconnect()
connect()
from expressvpn import wrapper
wrapper.random_connect()
from expressvpn import wrapper
wrapper.connect_alias('ch2')
try:
	wrapper.random_connect()
except ConnectException:
	print('Connect Exception')
import requests
ip = requests.get('https://api.ipify.org').text
ip
ls
import getpass
getpass.getpass()
p = getpass.getpass()
p
import os
os.system(f'sudo -S {p} kill -9 $(pgrep expressvpn)')
import subprocess
subprocess.call('ls -l')
subprocess.call('ls -l', shell=True)
subprocess.call('sudo kill -9 $(pgrep expressvpn)')
subprocess.call('sudo kill -9 $(pgrep expressvpn)', shell=True)
subprocess.call('pgrep expressvpn', shell=True)
import subprocess
subprocess.call('sudo kill -9 $(pgrep expressvpn)', shell=True)
subprocess.call('sudo connect usny', shell=True)
subprocess.call('expressvpn connect usny', shell=True)
subprocess.call('sudo connect usny', shell=True)
import subprocess
subprocess.call('sudo kill -9 $(pgrep expressvpn)', shell=True)
subprocess.call('expressvpn connect usny', shell=True)
import subprocess
import requests
ip = requests.get('https://api.ipify.org').text
            logging.info(f'Public IP address is: {ip}')
            print(f'Public IP address is: {ip}')
print(f'Public IP address is: {ip}')
import subprocess
import requests
ip = requests.get('https://api.ipify.org').text
# Default color levels for the color cube
cubelevels = [0x00, 0x5f, 0x87, 0xaf, 0xd7, 0xff]
# Generate a list of midpoints of the above list
snaps = [(x+y)/2 for x, y in zip(cubelevels, [0]+cubelevels)[1:]]
def rgb2short(r, g, b):
    """ Converts RGB values to the nearest equivalent xterm-256 color.
    """
    # Using list of snap points, convert RGB value to cube indexes
    r, g, b = map(lambda x: len(tuple(s for s in snaps if s<x)), (r, g, b))
    # Simple colorcube transform
    return r*36 + g*6 + b + 16
snaps = [(x+y)/2 for x, y in list(zip(cubelevels, [0]+cubelevels))[1:]]
rgb2short(140, 166, 108)
rgb2short(124,72,33)
rgb2short(24,87,85)
rgb2short(54, 128, 116)
rgb2short(124, 72, 33)
rgb2short(140, 166, 108)
line = 
line = '1
00:00:10,720 --> 00:00:13,350
line = '1\n00:00:10,720 --> 00:00:13,350\n[ring]'
line
print(line)
import re
re.match(r'\d+', line)
re_match = re.match(r'\d+', line)
re_match.group()
522/65
3205/648
costs = [625, 100, 12, 70, 275, 35, 60, 55, 50]
sum(costs)
rev = [17000, 580, 1900, 1900, 1900, 1900, 7000]
sum(rev)
totalRev = sum(rev)
totalRev
totalRev - 9846
import datetime from datetime
from datetime import datetime
datetime.now()
str(datetime.now())
from datetime import datetime
str(datetime.now()).replace(' ', '_')
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
onlyfiles = [f for f in listdir(mypath) if isfile(join('./log', f))]
mypath = './log'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
onlyfiles
sort(onlyfiles)
onlyfiles.sort()
onlyfiles
onlyfiles.sort(reverse=True)
onlyfiles
lastLog = onlyfiles.sort(reverse=True)[0]
lastLog = onlyfiles[0]
lastLog
from debug import setup
soup = setup()
from debug import setup
soup = setup()
from debug import setup
soup = setup()
from debug import setup
soup = setup()
from debug import setup
soup = setup()
soup
soup.find('ul', {'class': 'pagination'})
p = soup.find('ul', {'class': 'pagination'})
p
soup
soup.find('div', {'id': 'actionSaveSearchAffix'})
soup.find('div', {'id': 'bottom_paging'})
soup.find('div', {'class': 'big-screen-content'})
bigScreenContent = soup.find('div', {'class': 'big-screen-content'})
bigScreenContent.ul
pagination = soup.find('ul', {'class': 'pagination'})
pagination
pagination = soup.find_all('ul', {'class': 'pagination'})
pagination
pagination = soup.find('ul', {'class': 'pagination'})
soup.index('pagination')
str(soup).index('pagination')
str(soup)[208782:208800]
str(soup)[208782:209000]
str(soup)[208000:209000]
from debug import setup
soup = setup()
from debug import setup
soup = setup()
soup.find('span', {'id': 'searchHeader'})
soup.find('span', {'id': 'searchHeader'}).text
import re
re.findall(r'\d+', s)
headerText = soup.find('span', {'id': 'searchHeader'}).text
re.findall(r'\d+', headerText)
headerText = soup.find('span', {'id': 'searchHeader'}).text
re.findall(r'\d+', headerText[headerText.index('Page'):])
from debug import setup
soup = setup()
soup.findAll(text='No Results Found For Your Current Search')
not soup.findAll(text='No Results Found For Your Current Search')
re.findall(r'\d+', headerText[headerText.index('Page'):])
import re
headerText = soup.find('span', {'id': 'searchHeader'}).text
re.findall(r'\d+', headerText[headerText.index('Page'):])
pages = re.findall(r'\d+', headerText[headerText.index('Page'):])
len(pages)
pages = re.findall(r'\d+', headerText[headerText.index('Page 1 of'):])
page
pages
pages = re.findall(r'\d+', headerText[headerText.index('Page 1 of')+9:])
pages
int('0')
int('')
[][0]
range(36)
for i in range(3):
	print(i)
for i in range(0, 4):
	print(i)
for i in range(1, 4):
	print(i)
for i in range(2, 4):
	print(i)
from debug import setup
soup = setup()
from application.app.db_config import db_config
from landandfarm.app.db_config import db_config
from landwatch.app.db_config import db_config
from debug import setup
soup = setup()
results_el = soup.find('div', {'id': 'searchResultsGrid'})
results_el(
results_el
         property_card_el_list = results_el.find_all('article', {'class': 'property-card'})
property_card_el_list = results_el.find_all('article', {'class': 'property-card'})
property_card_el_list
len(property_card_el_list)
prop_card_el = property_card_el_list[0]
prop_card_el
prop_card_el.find('address', {'class': 'location'})
prop_card_el.find('address', {'class': 'location'}).text
re.findall(r'\d+', )
propCardText = prop_card_el.find('address', {'class': 'location'}).text
re.findall(r'\d+', propCardText)
import re
re.findall(r'\d+', propCardText)
re.findall(r'\d+', propCardText[propCardText.index('TN'):])
[][0]
prop_card_el = property_card_el_list[11]
prop_card_el.find('address', {'class': 'location'})
prop_card_el = property_card_el_list[12]
prop_card_el.find('address', {'class': 'location'})
from debug import setup
soup = setup()
propCardText = prop_card_el.find('address', {'class': 'location'}).text
results_el = soup.find('div', {'id': 'searchResultsGrid'})
property_card_el_list = results_el.find_all('article', {'class': 'property-card'})
prop_card_el = property_card_el_list[1]
propCardText = prop_card_el.find('address', {'class': 'location'}).text
re.findall(r'\d+', propCardText[propCardText.index('AZ'):])
import re
re.findall(r'\d+', propCardText[propCardText.index('AZ'):])
'' == True
'' == False
print('yes' if '' else 'no')
print('yes' if not '' else 'no')
28700/37
from debug import setup
soup = setup()
         resultsElement = soup.find('div', {'id': 'searchResultsGrid'})
resultsElement = soup.find('div', {'id': 'searchResultsGrid'})
propertyCardElementList = resultsElement.find_all('article', {'class': 'property-card'})
propertyCardElement = propertyCardElementList[0]
propertyCardElemen.find('a', {'class', 'property-card--property-link'})
propertyCardElement.find('a', {'class', 'property-card--property-link'})
propertyLinkElement = propertyCardElement.find('a', {'class', 'property-card--property-link'})
propertyLinkElement['href']
propertyLinkElement = propertyCardElement.find('a', {'class', 'property-card--property-link'})
propertyLinkElement['href']
from debug import setup
import time
import concurrent.futures
import time
t = time.sleep
t
t = time.sleep()
t = time.sleep(1)
t
t is None
l = [1,2,3,4,5,6]
map(lambda num: {'state': 'CO', 'num': num}, l)
list(map(lambda num: {'state': 'CO', 'num': num}, l))
s = 'Wyoming Land for Sale between $5K and $30K'
s.index('Page 1 of')
'Page 1 of' in s
l = [1,2,3,4,5,6]
l[0:3:]
l[0:3::]
l[0:3:-1]
l[0:3:len(l)-1]
l[0:2:1]
l = None
l
[i for i in l]
total_pop = 3843
3757/total_pop
16/total_pop
10/total_pop
1885/total_pop
381+281
662/total_pop
662+172
834/total_pop
'America/Indiana/Indianapolis'
len('America/Indiana/Indianapolis')
   insert_cmd = 'INSERT INTO zip_codes (%s) VALUES %s ON CONFLICT DO NOTHING'
insert_cmd = 'INSERT INTO zip_codes (%s) VALUES %s ON CONFLICT DO NOTHING'
insert_cmd
insert_cmd = f'INSERT INTO {table_name} (%s) VALUES %s ON CONFLICT DO NOTHING'
table_name = 'zip_codes'
insert_cmd = f'INSERT INTO {table_name} (%s) VALUES %s ON CONFLICT DO NOTHING'
insert_cmd
l = ['a', 'b', 'c'
l = ['a', 'b', 'c']
l
i = 0
l[i]
l[i+=1]
l[(i+=1)]
i
i+=1
i
++i
i
l = ['a', 'b', 'c']
i = 0
f'i is {i+=1}'
i
f'i is {i += 1}'
l = ['a', 'b', 'c']
range(len(l))
[ i for i in range(len(l))]
int('')
int('1')
int('')
'' == True
'' == False
'' is False
a = 0
if a:
	print('a')
a = 1
if a:
	print('a')
d = {}
d['a'] = 1
d
from station_lat_long_voronoi import get_random_point_array 
point
point_arr = get_random_point_array()
point_arr
from station_lat_long_voronoi import get_random_point_array 
point_arr = get_random_point_array()
point_arr
from station_lat_long_voronoi import get_random_point_array 
point_arr = get_random_point_array()
point_arr
rom scipy.spatial import Voronoi, voronoi_plot_2d
from scipy.spatial import Voronoi, voronoi_plot_2d
vor = Voronoi(point_arr)
vor
vor.vertices
import matplotlib.pyplot as plt
fig = voronoi_plot_2d(vor)
plt.show()
plt.savefig("vor.png")
from datetime import date
today = date.today()
today
today.strftime('%d/%m/%y')
from datetime import datetime
datetime.strptime('3/9/20', '%d/%m/%y')
today = datetime.strptime('4/9/20', '%d/%m/%y')
today
today.strftime('%d/%m/%y')
import datetime from datetime
from datetime input datetime
from datetime import datetime
today = datetime()
today = datetime.date.today()
import datetime
today = datetime.date.today()
jan_1_20 = datetime.date.strptime('2020-01-01')
jan_1_20 = datetime.strptime('2020-01-01')
jan_1_20 = datetime.datetime.strptime('2020-01-01')
jan_1_20 = datetime.datetime.strptime('2020-01-01', '%Y-%m-%d')
jan_1_20
today
today = datetime(2020, 1, 1)
today = datetime.datetime(2020, 1, 1)
today
today = datetime.datetime(2020, 9, 1)
today = datetime.datetime(2020, 9, 5)
today
jan_1_20
d1 = datetime.datetime(2020, 1, 1)
d2 = datetime.datetime(2020, 9, 5)
d2 - d1
(d2 - d1).days
datetime.datetime.now()
'EUREKA WEATHER FORECAST OFFICE WOODLEY ISLAND, CA US'
len('EUREKA WEATHER FORECAST OFFICE WOODLEY ISLAND, CA US')
l = [1,2,3,4,5]
l[0::3]
l[:3]
l[:2]
from datetime import datetime, timedelta
start_date = datetime.now()
end_date = start_date
start_date = end_date - timedelta(days=365)
start_date_str = start.date.strftime('%Y-%m-%d')
start_date_str = start_date.strftime('%Y-%m-%d')
start_date_str
end_date_str = end_date.strftime('%Y-%m-%d')
end_date_str
start_date = datetime.today().replace(day=1)
end_date = start_date
start_date = end_date - timedelta(days=365)
start_date_str = start_date.strftime('%Y-%m-%d')
end_date_str = end_date.strftime('%Y-%m-%d')
start_date_str
end_date_str
start_date = datetime.today().replace(day=1)
datetime.today().replace(day=1).strftime('%Y-%m-%d')
from dateutil.relativedelta import relativedelta
d1 = datetime.today().replace(day=1) - relativedelta(years=1)
d1.strftime('%Y-%m-%d')
from datetime import datetime
date_str = '2019-09-07T00:00:00'
date = datetime.strptime(date_str, '%Y-%m-%dT%H%M%S')
date = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S')
date.month
[i for i in range(1,13)]
sum([])
0/0
if not len([]): print('len 0')
from datetime import datetime
datetime.now
datetime.now()
datetime.now().strftime()
datetime.now().strftime('%H:%M:%S')
from datetime import datetime
t1 = datetime.now()
t2 = datetime.now()
str(t2 - t1)
import random
random()
random.random()
import random
random.randrange(.5, 2)
random.randrange(1, 2)
random.random() * 3 + 1
random.random() * 3 
random.random()+1 
new_value = ( (old_value - old_min) / (old_max - old_min) ) * (new_max - new_min) + new_min
old_min = 0.001
old_max = 1
new_max = 2
new_min = .5
 ( (old_value - old_min) / (old_max - old_min) ) * (new_max - new_min) + new_min
( (old_value - old_min) / (old_max - old_min) ) * (new_max - new_min) + new_min
random.random() * (new_max - new_min) + new_min
import random
random.random() * (3 - 1) + 1
print(None)
print(f'{None}')
print(f'{''}')
print(f'{""}')
41+45+50+49+48
96+98+100+107+108
96+100+103+103+106
100+104+104+103+106
60*4
+32
60*4+32
272 / 233
6*60+39
399/509
7*60+21
7*60+41
461/508
6*60+57
417/517
from datetime import datetime
t1 = datetime.now()
t2 = datetime.now()
(t2 - t1).seconds
(t2 - t1).milliseconds
(t2 - t1)
(t2 - t1).microseconds
(t2 - t1).microseconds / 1000
(t2 - t1).microseconds / 1000000
(t2 - t1).microseconds / 100000
(t2 - t1).total_seconds
(t2 - t1).total_seconds()
l = ['a', 'b', 'c', 'd']
l[:3]
from datetime import datetime
t1 = datetime.now()
t2 = datetime.now()
(t2 - t1).total_seconds()
(3000 - 28848) / 28848
(3000 - 28848) / 28848 * 100
abs(3000 - 28848) / 28848 * 100
import os
import matplotlib.pyplot as plt
import geopandas as gpd
import earthpy as et
et.data.get_data('usdm_20200901')
gpd.read_file('./usdm_20200901/USDM_20200901.sh')
gpd.read_file('/home/enigmaticmustard/projects/gis_python/usdm_20200901/USDM_20200901.sh')
gpd.read_file('/home/enigmaticmustard/projects/gis_python/usdm_20200901/USDM_20200901.shp')
shp_file = gpd.read_file('/home/enigmaticmustard/projects/gis_python/usdm_20200901/USDM_20200901.shp')
shp_file.head(3)
shp_file.head(5)
shp_file.class()
type(shp_file)
shp_file.total_bounds
shp_file.crs
shp_file.geom_type
shp_file.shpe
shp_file.shape
fig, ax = plt.subplots(figsize = (10,10))
shp_file.plot(ax=ax)
plt.show()
plt
plt.savefig('dm_test.png')
shp_file.head(7)
shp_file.plot(column='DM',categorical=True,legend=True,figsize=(10,6),markersize=45,cmap="Set2",ax=ax)
plt.savefig('dm_test.png')
shp_file.crs
import readline
readline.get_history_length()
readline.get_current_history_length()
readline.get_current_history_length(1)
readline.get_history_item(1)
[i for i in range(800, 807)
]
hist_len = readline.get_current_history_length()
hist_len
hist_list = [readline.get_history_item(line) for line in range(hist_len-50, hist_len)]
hist_l
hist_list
with open('./goepandas_demo.py', 'w') as f:
	for hist in hist_list:
		f.write(hist)
with open('./geopandas_demo.py', 'w') as f:
	for hist in hist_list:
		f.write(hist)
		f.wriet('\n')
		f.write('\n')
with open('./geopandas_demo.py', 'w') as f:
	for hist in hist_list:
		f.write(hist)
		f.write('\n')
shp_file.head(10)
shp_file.head(6)
shp_file
type(shp_file)
shp_file.head(6)
shp_file.head(5)
type(shp_file)
shp_file.geom_type
shp_file.geometry.name
shp_file.geometry
et.data.get_data('cb_2019_us_state_500k')
shp_file
type(shp_file)
os.curdir
os.path
drought_monitor_gdf = gpd.read_file(
)
drought_monitor_gdf = gpd.read_file('./usdm_20200901/USDM_20200901.shp')
drought_monitor_gdf.head()
states_us_gdf = gpd.read_file('./cb_2019_us_state_500k.shp')
states_us_gdf = gpd.read_file('./cb_2019_us_state_500k/cb_2019_us_state_500k.shp')
states_us_gdf.head()
states_us_gdf.head(10)
states_us_gdf.columns
states_us_gdf.crs
drought_monitor_gdf.crs
states_us_gdf.crs
import numpy as np
states_us_gdf.crs
fig, ax = plt.subplot(figsize=(12, 8))
fig, ax = plt.subplots(figsize=(12, 8))
states_us_gdf.plot(cmap='States', ax=ax, alpha=.5)
states_us_gdf.plot(ax=ax)
drought_monitor_gdf.plot(ax=ax)
plt.savefig('drought_states_no_reproject.png')
drought_monitor_gdf.plot(color='lightgrey', edgecolor=black, ax=ax, alpha=.5)
drought_monitor_gdf.plot(color='lightgrey', edgecolor='black', ax=ax, alpha=.5)
drought_monitor_gdf.columns
drought_monitor_gdf.plot(ax=ax)
plt.savefig('drought_states_no_reproject.png')
drought_monitor_gdf
drought_monitor_gdf.plot(column='DM',categorical=True,legend=True,figsize=(10,6),markersize=45,cmap="Set2",ax=ax)
plt.savefig('drought_states_no_reproject.png')
states_us_gdf
states_us_gdf.name
states_us_gdf
type(states_us_gdf)
states_us_gdf['Name']
states_us_gd
states_us_gdf['NAME']
states_us_gdf.area
colorado_gdf = states_us_gdf[states_us_gdf['NAME'] == 'California']
colorado_gdf
colorado_gdf['NAME']
california_gdf = states_us_gdf[states_us_gdf['NAME'] == 'California']
california_gdf['NAME']
ca_dm_gdf = gpd.overlay(california_gdf, drought_monitor_gdf, )
california_gdf.crs
drought_monitor_gdf.crs
dm_reproj_gdf = drought_monitor_gdf.to_crs('epsg:4269')
dm_reproj_gdf
dm_reproj_gdf.crs
california_gdf.crs
dm_reproj_gdf.plot(column='DM',categorical=True,legend=True,figsize=(10,6),markersize=45,cmap="Set2",ax=ax)
dm_reproj_gdf.plot(color='lightgrey', edgecolor='black', ax=ax, alpha=.5)
california_gdf.plot(column='DM',categorical=True,legend=True,figsize=(10,6),markersize=45,cmap="Set2",ax=ax)
california_gdf.plot(color='lightgrey', edgecolor='black', ax=ax, alpha=.5)
dm_reproj_gdf.plot(column='DM',categorical=True,legend=True,figsize=(10,6),markersize=45,cmap="Set2",ax=ax)
plt.savefig('ca_dm.png')
type(plt)
plt
plt.cla()
plt.savefig('ca_dm.png')
dm_reproj_gdf.plot(column='DM',categorical=True,legend=True,figsize=(10,6),markersize=45,cmap="Set2",ax=ax)
california_gdf.plot(color='lightgrey', edgecolor='black', ax=ax, alpha=.5)
plt.savefig('ca_dm.png')
california_gdf.crs
ca_dm_intersection_gdf = gpd.overlay(california_gdf, dm_reproj_gdf, how='intersection')
with open('./python_hist.py', 'w') as f:
	for hist in [readline.get_history_item(line) for line in range(readline.get_current_history_length()-50, readline.get_current_history_length())]:
		print(hist)
		print('\n')
with open('./python_hist.py', 'w') as f:
	for hist in [readline.get_history_item(line) for line in range(readline.get_current_history_length()-50, readline.get_current_history_length())]:
		f.write(hist)
		f.write('\n')
with open('./python_hist.py', 'w') as f:
	for hist in [readline.get_history_item(line) for line in range(readline.get_current_history_length()-100, readline.get_current_history_length())]:
		f.write(hist)
		f.write('\n')
import rasterio
src = rasterio.open('wildfire_hazard_potential_2018.tiff')
import rasterio
src = rasterio.open('wildfire_hazard_potential_2018.tiff')
import rasterio
src = rasterio.open('')
src = rasterio.open('wildfire_hazard_potential_2018.tif')
import rasterio
src = rasterio.open('whp2018_cls')
src
src.name
src.mode
src.count
src.width
src.height
src.bounds
src.crs
from matplotlib import pyplot
pyplot.imshow(src.read(1))
pyplot.savefig('rasterio_test.png')
src.read(1)
pyplot.plot(src.read(1))
pyplot.savefig('rasterio_test.png')
from rasterio.plot import show
show(src)
    fig, ax = plt.subplots(figsize=(12, 8))
fig, ax = pyplot.subplots(figsize=(12, 8))
pyplot.plot(src.read(1), categorical=True,legend=True,figsize=(10,6),markersize=45,cmap="Set2",ax=ax, alpha=.5, edgecolor='black');
pyplot.plot(src.read(1),legend=True,figsize=(10,6),markersize=45,cmap="Set2",ax=ax, alpha=.5, edgecolor='black');
pyplot.plot(src.read(1), cmap="Set2")
pyplot.imshow(src.read(1), cmap='Set2')
pyplot.savefig('rasterio_test.png')
from rasterio import MemoryFile
pyplot.plot(src.read(1), cmap="Set2")
pyplot.plot(src.read(1))
pyplot.plot()
from rasterio.plot import show
pyplot.show()
matplotlib.user('TkAgg')
import matplotlib
matplotlib.user('TkAgg')
matplotlib.use('TkAgg')
pyplot.show()
pyplot.plot(src.read(1))
from rasterio.plot import show
from urllib.request import urlopen
url = 'https://apps.fs.usda.gov/fsgisx01/rest/services/RDW_Wildfire/RMRS_WildfireHazardPotential_2018/ImageServer'
tif_bytes = urlopen(url).read()
with MemoryFile(tif_bytes) as memfile:
	with memfile.open() as dataset:
		print(dataset.profile)
		show(dataset)
with MemoryFile(tif_bytes) as memfile:
	with memfile.open() as dataset:
		print(dataset.profile)
tif_bytes
url
src.width
src.height
src = rasterio.open('whp2018_cls')
src
scr.colorinterp[0]
src.colorinterp[0]
src.colorinterp
profile = src.profile
profile['photometric'] = 
profile['photometric'] = 'RGB'
src.write(src.read())
with rasterio.open('whp2018_cls', 'w', **profile) as dst:
	dst.write(src.read())
\h
history()
from gis-import.plot_counties_whp import reproject_raster_from_shp_crs
from gis_import.plot_counties_whp import reproject_raster_from_shp_crs
raster_file = './data/wildfire_hazard_potential_2018.tif'
shp_file = './data/census_boundaries_2019/counties.zip'
reproject_raster_from_shp_crs(raster_file, shp_file)
shp_file = 'zip//./data/census_boundaries_2019/counties.zip'
reproject_raster_from_shp_crs(raster_file, shp_file)
shp_file = 'zip://./data/census_boundaries_2019/counties.zip'
reproject_raster_from_shp_crs(raster_file, shp_file)
from gis_import.plot_counties_whp import reproject_raster_from_shp_crs
reproject_raster_from_shp_crs(raster_file, shp_file)
import rasterio
rasterio.crs.CRS()
rasterio.crs.CRS
import geopandas
geopandas.read_file(shp_file)
counties = geopandas.read_file(shp_file)
dst_crs = rasterio.crs.CRS.from_dict(counties.crs)
counties.crs
type(counties.crs)
wildfire_raster = rasterio.open(raster_file)
raster_file
wildfire_raster = rasterio.open(raster_file)
ls
from gis_import.plot_counties_whp import reproject_raster_from_shp_crs
reproject_raster_from_shp_crs(raster_file, shp_file)
from gis_import.plot_counties_whp import reproject_raster_from_shp_crs
reproject_raster_from_shp_crs(raster_file, shp_file)
from gis_import.plot_counties_whp import reproject_raster_from_shp_crs
raster_file = './data/whp_2018_classified/whp2018_cls'
shp_file = 'zip://./data/census_boundaries_2019/counties.zip'
reproject_raster_from_shp_crs(raster_file, shp_file)
import geopandas
import rasterio
counties = geopandas.read_file(shp_file_
counties = geopandas.read_file(shp_file)
counties_gdf = geopandas.read_file(shp_file)
wildfire_raster = rasterio.open(raster_file)
wildfire_raster.crs
counties.crs
wildfire_raster_str = 'PROJCS["unnamed",GEOGCS["NAD83",DATUM["North_American_Datum_1983",SPHEROID["GRS 1980",6378137,298.257222101,AUTHORITY["EPSG","7019"]],TOWGS84[0,0,0,0,0,0,0],AUTHORITY["EPSG","6269"]],PRIMEM["Greenwich",0,AUTHORITY["EPSG","8901"]],UNIT["degree",0.0174532925199433,AUTHORITY["EPSG","9122"]],AUTHORITY["EPSG","4269"]],PROJECTION["Albers_Conic_Equal_Area"],PARAMETER["standard_parallel_1",29.5],PARAMETER["standard_parallel_2",45.5],PARAMETER["latitude_of_center",23],PARAMETER["longitude_of_center",-96],PARAMETER["false_easting",0],PARAMETER["false_northing",0],UNIT["METERS",1]]'
rasterio.crs.CRS.from_wkt(wildfire_raster_str)
type(wildfire_raster.crs)
type(counties.crs)
import pyproj
counties_rio_crs = rasterio.crs.CRS.from_user_input(counties.crs)
counties_rio_crs
shp_file = 'zip://./data/census_boundaries_2019/counties.zip'
raster_file = './data/whp_2018_classified/whp2018_cls'
from gis_import.plot_counties_whp import reproject_raster_from_shp_crs
reproject_raster_from_shp_crs(raster_file, shp_file)
import geopandas
import rasterio
counties_gdf = geopandas.read_file(shp_file)
wildfire_raster = rasterio.open(raster_file)
wildfire_raster.crs
counties_gdf.crs
type(counties_gdf.crs)
type(wildfire_raster.crs)
counties_rio_crs = rasterio.crs.CRS.from_user_input(counties_gdf.crs)
counties_rio_crs
type(counties_rio_crs)
type(wildfire_raster.crs)
wildfire_raster.crs
from rasterio.warp import calculate_default_transform
calculate_default_transform(wildfire_raster.crs, , wildfire_raster.width, wildfire_raster.height, *wildfire_raster.bounds)
import pyproj
pyproj_crs = pyproj.crs.CRS.from_epsg(4326)
type(pyproj)
pyproj_crs
rio_crs = rasterio.crs.CRS.from_user_input(pyproj_crs)
rio_crs
from distutils.version import LooseVersion
if LooseVersion(rasterio.__gidal_version__) < LooseVersion('3.0.0')
if LooseVersion(rasterio.__gidal_version__) < LooseVersion('3.0.0'):
    rio_crs = rasterio.crs.CRS.from_wkt(pyproj_crs.to_wkt(pyproj.enums.WktVersion.WKT1_GDAL))
else:
    rio_crs = rasterio.crs.CRS.from_wkt(pyproj_crs.to_wkt())
    
if LooseVersion(rasterio.__gdal_version__) < LooseVersion('3.0.0'):
    rio_crs = rasterio.crs.CRS.from_wkt(pyproj_crs.to_wkt(pyproj.enums.WktVersion.WKT1_GDAL))
else:
    rio_crs = rasterio.crs.CRS.from_wkt(pyproj_crs.to_wkt())
    
rio_crs
type(rio_crs)
pyproj_crs.to_wkt()
rio_crs = rasterio.crs.CRS.from_wkt(pyproj_crs.to_wkt())
rio_crs
rio_crs = rasterio.crs.CRS.from_user_input((pyproj_crs)
rio_crs = rasterio.crs.CRS.from_user_input(pyproj_crs)
rio_crs
rio_crs = rasterio.crs.CRS.from_user_input(pyproj_crs)
rio_crs
counties_rio_crs = rasterio.crs.CRS.from_user_input(counties_gdf.crs)
counties_rio_crs
rio_crs
calculate_default_transform(wildfire_raster.crs, rio_crs, wildfire_raster.width, wildfire_raster.height, *wildfire_raster.bounds)
calculate_default_transform(wildfire_raster.crs, pyproj_crs.to_wkt(), wildfire_raster.width, wildfire_raster.height, *wildfire_raster.bounds)
pyproj_crs.to_wkt()
wildfire_raster.crs
if LooseVersion(rasterio.__gdal_version__) < LooseVersion('3.0.0'):
    rio_crs = rasterio.crs.CRS.from_wkt(pyproj_crs.to_wkt(pyproj.enums.WktVersion.WKT1_GDAL))
else:
    rio_crs = rasterio.crs.CRS.from_wkt(pyproj_crs.to_wkt())
    
rio_crs
calculate_default_transform(wildfire_raster.crs, rio_crs, wildfire_raster.width, wildfire_raster.height, *wildfire_raster.bounds)
raster_file = './data/whp_2018_classified/whp2018_cls'
shp_file = 'zip://./data/census_boundaries_2019/counties.zip'
from rasterio.warp import calculate_default_transform
from gis_import.plot_counties_whp import reproject_raster_from_shp_crs
reproject_raster_from_shp_crs(raster_file, shp_file)
from distutils.version import LooseVersion
reproject_raster_from_shp_crs(raster_file, shp_file)
raster_file = './data/whp_2018_classified/whp2018_cls'
shp_file = 'zip://./data/census_boundaries_2019/counties.zip'
from gis_import.plot_counties_whp import reproject_raster_from_shp_crs
reproject_raster_from_shp_crs(raster_file, shp_file)
from gis_import.plot_counties_whp import reproject_raster_from_shp_crs
reproject_raster_from_shp_crs(raster_file, shp_file)
raster_file = './data/whp_2018_classified/whp2018_cls'
shp_file = 'zip://./data/census_boundaries_2019/counties.zip'
from gis_import.plot_counties_whp import reproject_raster_from_shp_crs
reproject_raster_from_shp_crs(raster_file, shp_file)
import rasterio
wildfire_raster = raster.open(raster_file)
wildfire_raster = rasterio.open(raster_file)
rasterio.band(wildfire_raster, 1)
rasterio.band(wildfire_raster, 2)
rasterio.band(wildfire_raster, 3)
rasterio.band(wildfire_raster, 4)
rasterio.band(wildfire_raster, 5)
rasterio.band(wildfire_raster, 6)
rasterio.band(wildfire_raster, 7)
wildfire_raster.count
shp_file = 'zip://./data/census_boundaries_2019/counties.zip'
raster_file = './data/whp_2018_classified/whp2018_cls'
from gis_import.plot_counties_whp import reproject_raster_from_shp_crs
reproject_raster_from_shp_crs(raster_file, shp_file)
shp_file = 'zip://./data/census_boundaries_2019/counties.zip'
raster_file = './data/whp_2018_classified/whp2018_cls'
from gis_import.plot_counties_whp import reproject_raster_from_shp_crs
reproject_raster_from_shp_crs(raster_file, shp_file)
import rasterio
rasterio.band.__class__
rasterio.band.__class__()
rasterio.band()
whp_raster = raster.open(raster_file)
whp_raster = rasterio.open(raster_file)
whp_raster
rasterio.band(whp_raster)
rasterio.band(whp_raster, 1)
whp_raster.shape
import numpy
import numpy as np
destinaton = np.zeros(whp_raster.shape, np.uint8)
destinaton
destinaton.shape
whp_raster.shape
raster_file = './data/whp_2018_classified/whp2018_cls'
shp_file = 'zip://./data/census_boundaries_2019/counties.zip'
from gis_import.plot_counties_whp import reproject_raster_from_shp_crs
raster_file = './data/whp_2018_classified/whp2018_cls'
shp_file = 'zip://./data/census_boundaries_2019/counties.zip'
from gis_import.plot_counties_whp import reproject_raster_from_shp_crs
reproj_raster = reproject_raster_from_shp_crs(raster_file, shp_file)
shp_file = 'zip://./data/census_boundaries_2019/counties.zip'
raster_file = './data/whp_2018_classified/whp2018_cls'
from gis_import.plot_counties_whp import reproject_raster_from_shp_crs
reproj_raster = reproject_raster_from_shp_crs(raster_file, shp_file)
reproj_raster
assert reproj_raster.any()
assert not reproj_raster.all()
type(reproj_raster)
import rasterio
whp_raster = rasterio.open(raster_file)
whp_raster
whp_raster.dataset_mask()
type(whp_raster)
whp_raster.xy()
whp_raster.indexes
whp_raster.units
whp_raster.res
whp_raster.band(1)
rasterio.band(whp_raster, 1)
whp_bandrasterio.band(whp_raster, 1)
whp_band = rasterio.band(whp_raster, 1)
whp_band
whp_band.ds
whp_band.dtype
whp_band.shape
whp_band.index(10, 10)
whp_band.index(10)
whp_band.index((10, 10))
whp_band.index(1)
whp_band.index(2)
whp_band_index_1 = whp_band.index(1)
whp_band_index_1
type = (whp_band_index_1)
type(whp_band_index_1)
import types
types
types.type
type
import rasterio
reproj_raster = rasterio.open('/tmp/reproj.tf')
reproj_raster = rasterio.open('/tmp/reproj.tif')
reproj_raster
reporj_raster.crs
reproj_raster.crs
import get_datasets from plot_counties_whp
from plot_counties_whp import get_datasets()
from plot_counties_whp import get_datasets
counties, whp = get_datasets()
counties
whp
import rasterio
import geopandas
import matplotlib.pyplot as plt
import rasterio.plot as rio_plt
ls
fig, ax = plt.subplots(figsize=(12, 8))
rasterio.plot.show(raster, ax=ax)
rasterio.plot.show(whp, ax=ax)
plt.show()
counties.plot(ax=ax, facecolor='none', edgecolor='black')
plt.show()
from plot_counties_whp import get_datasets
counties, whp = get_datasets()
import matplotlib.pyplot as plt
import rasterio.plot as rio_plt
rio_plt.show(whp, ax=ax)
fig, ax = plt.subplots(figsize=(20, 20))
rio_plt.show(whp, ax=ax)
counties.plot(ax=ax, facecolor='none', edgecolor='black')
plt.show()
import matplotlib.pyplot as plt
from plot_counties_whp import get_datasets
counties, whp = get_datasets()
counties.plot(ax=ax, facecolor='none', edgecolor='black')
fig, ax = plt.subplots(figsize=(20, 20))
counties.plot(ax=ax, facecolor='none', edgecolor='black')
plt.show()
    plt.savefig('/home/enigmaticmustard/projects/landwatch/data/graphs/counties.png')
plt.savefig('/home/enigmaticmustard/projects/landwatch/data/graphs/counties.png')
import rasterio.plot as rio_plt
rio_plt.show(whp, ax=ax)
plt.savefig('/home/enigmaticmustard/projects/landwatch/data/graphs/whp.png')
rio_plt(whp, ax=ax)
rio_plt.show(whp, ax=ax)
plt.savefig('/home/enigmaticmustard/projects/landwatch/data/graphs/whp.png')
plt.show()
whp
counties
rio_plt.show(whp, ax=ax)
plt.show()
history(10)
history(1)
import site
site.getusersitepackages()
history()
from plot_counties_whp import get_datasets
from plot_counties_whp.gis_import import get_datasets
from gis_import.plot_counties_whp import get_datasets
counties, whp = get_datasets()
counties
type(counties
)
from gis_import.plot_counties_whp import get_datasets
counties, whp = get_datasets()
s = set(['https://wcca.wicourts.gov/caseDetail.html?caseNo=2011CF002590&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2010CF005773&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2010CF001779&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2011CF004596&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2011CF004595&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2012CF002806&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2012CF002434&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2013CF000044&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2014CF005648&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2019CF001367&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2017CF000723&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2017CF000723&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2018CF000155&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2017CF005843&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2017CF002878&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2017CF002552&countyNo=40&index=0&isAdvanced=true&mode=details']
)
s
len(s)
l = ['https://wcca.wicourts.gov/caseDetail.html?caseNo=2011CF002590&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2010CF005773&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2010CF001779&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2011CF004596&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2011CF004595&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2012CF002806&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2012CF002434&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2013CF000044&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2014CF005648&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2019CF001367&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2017CF000723&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2017CF000723&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2018CF000155&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2017CF005843&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2017CF002878&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2017CF002552&countyNo=40&index=0&isAdvanced=true&mode=details']
len(l)
print(s)
[x for x in l if x not in s]
len(l)
import collections
[i for i, count in collections.Counter(l).items() if count > 1]
l = ['https://wcca.wicourts.gov/caseDetail.html?caseNo=2019CM002734&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2019CM001708&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2019CM000794&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2019CM000705&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2018CM004647&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2018CM003465&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2018CM001944&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2018CM000397&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2017CM004042&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2017CM003852&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2017CM003328&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2017CM001492&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2016CM003656&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2015CM004367&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2015CM003057&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2015CM003460&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2015CM003318&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2014CM004453&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2014CM002925&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2013CM005000&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2013CM004045&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2013CM002779&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2013CM000655&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2012CM006283&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2012CM000353&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2011CM004024&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2011CM003023&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2011CM001928&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2010CM006212&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2010CM006127&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2010CM000200&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2010CM000175&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2009CM005435&countyNo=40&index=0&isAdvanced=true&mode=details']
[i for i, count in collections.Counter(l).items() if count > 1]
l
len (l)
[i for i, count in collections.Counter(l).items() if count > 1]
l = ['https://wcca.wicourts.gov/caseDetail.html?caseNo=2011CF002970&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2011CF001614&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2011CF000781&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2010CF005843&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2010CF004991&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2010CF003118&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2010CF002625&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2010CF001779&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2011CF005665&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2011CF005050&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2012CF001309&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2012CF000328&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2012CF004658&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2012CF003968&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2012CF004742&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2012CF003894&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2012CF003817&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2012CF003094&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2012CF005128&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2013CF001006&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2013CF002108&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2013CF002065&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2013CF002012&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2013CF001643&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2013CF004381&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2013CF004247&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2013CF004275&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2014CF000950&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2014CF000575&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2013CF005705&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2013CF005457&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2013CF005075&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2014CF002706&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2014CF001432&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2014CF005404&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2014CF005077&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2014CF004956&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2014CF004839&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2014CF004638&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2014CF004636&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2015CF003826&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2015CF003143&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2017CF002284&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2017CF001294&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2017CF001191&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2017CF000351&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2016CF004334&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2016CF003175&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2016CF002474&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2016CF001889&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2016CF001710&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2016CF000775&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2016CF000502&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2016CF000213&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2016CF000178&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2017CF002311&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2017CF002284&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2017CF002223&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2017CF001294&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2017CF001191&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2017CF001035&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2017CF005301&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2017CF005223&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2017CF004370&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2017CF004028&countyNo=40&index=0&isAdvanced=true&mode=details', 'https://wcca.wicourts.gov/caseDetail.html?caseNo=2017CF003078&countyNo=40&index=0&isAdvanced=true&mode=details']
l
[i for i, count in collections.Counter(l).items() if count > 1]
45*11
from gis_import.plot_counties_whp import get_datasets
counties, whp = get_datasets()
whp
counties
whp
counties
raster = whp
raster
x_range = int(abs(raster.bounds.left) + abs(raster.bounds.right))
y_range = int(abs(raster.bounds.bottom) + abs(raster.bounds.top))
for i in range(x_range):
    for j in range(y_range):
import random
for i in range(10):
    for j in range(10):
        x = random.randrange(x_range)
        y = random.randrange(y_range)
        sample = raster.sample([(i, j)])
        print(f'({x}, {y}): {sample}')
        
    
import geopandas as gpd
counties
counties.columns
counties
zip_codes = counties
zip_codes
zip_code_95444
zip_codes
type(zip_codes
)
zip_code_95444 = zip_codes.loc[zip_codes['ZCTA5CE10'] == '95444']
zip_code_95444
zip_code_95444.representative_point()
zip_code_95444.x
zip_code_95444.explode()
zip_code_95444.geometry
type(zip_code_95444.geometry)
zip_code_95444.geometry.x
zip_code_95444.geometry
zip_code_95444.geometry.centroid
zip_code_95444.geometry.centroid.x
zip_code_95444.geometry.items()
zip_code_95444.geometry.iteritems()
zip_code_95444
type(zip_code_95444)
[list(zip_code_95444.geometry.exterior[row_id].coords) for row_id in range(zip_code_95444.shape[0])]
zip_code_95444.shape[0]
[zip_code_95444.geometry.exterior[row_id].coords for row_id in range(zip_code_95444.shape[0])]
zip_code_95444.geometry.exterior[0].coords
zip_code_95444.geometry.exterior
zip_code_95444.geometry.exterior[1]
zip_code_95444.geometry.exterior
zip_code_95444.geometry.exterior.coords
zip_code_95444.geometry.exterior
type(zip_code_95444.geometry.exterior)
zip_code_95444.geometry.exterior.exterior
zip_code_95444.geometry.shape
zip_code_95444.geometry[1]
zip_code_95444.geometry.shape[1]
zip_code_95444.geometry.shape[0]
zip_code_95444.geometry
zip_code_95444.geometry.exterior
zip_code_95444.geometry.exterior.coords
zip_code_95444.geometry.iloc[0]
zip_code_95444.geometry.iloc[0].coords
type(zip_code_95444.geometry.iloc[0])
zip_code_95444.geometry.iloc[0]
zip_code_95444.geometry.coords
type(zip_code_95444.geometry)
type(zip_code_95444.geometry.exterior)
type(zip_code_95444.geometry.iloc[0])
zip_code_95444.geometry.iloc[0].coords
zip_code_95444.geometry.type
zip_code_95444.geometry)
type(zip_code_95444.geometry)
type(zip_code_95444.geometry.exterior)
type(zip_code_95444.geometry.iloc[0])
type(zip_code_95444.geometry)
zip_code_95444['geometry']
zip_code_95444['geometry'].coords
type(zip_code_95444['geometry'])
type(zip_code_95444.geometry)
zip_code_95444['geometry'].coords
zip_code_95444['geometry'].iloc[0]
zip_code_95444['geometry'].iloc[0].coords
zip_code_95444['geometry'].iloc[0]
zip_code_95444['geometry'].iloc[0]._get_coords()
zip_code_95444['geometry'].iloc[0].__geo_interface__
zip_code_95444['geometry'].iloc[0]['coordinates']
zip_code_95444['geometry'].iloc[0].coordinates
zip_code_95444['geometry'].iloc[0].exterior
zip_code_95444['geometry'].iloc[0].exterior.coords
zip_code_95444['geometry'].iloc[0].exterior.coords.xy
zip_code_95444['geometry'].iloc[0].interiors
zip_code_95444['geometry'].iloc[0].interiors.len
zip_code_95444['geometry'].iloc[0].interiors.length
len(zip_code_95444['geometry'].iloc[0].interiors)
len(zip_code_95444['geometry'].iloc[0].exteriors)
len(zip_code_95444['geometry'].iloc[0].exterior)
len(zip_code_95444['geometry'].iloc[0].interiors)
zip_code_95444['geometry'].iloc[0].interiors
zip_code_95444['geometry'].iloc[0].interiors[0]
[i for i in zip_code_95444['geometry'].iloc[0].interiors]
zip_code_95444['geometry'].iloc[0].exterior.coords.xy
zip_codes
raster
raster.index(0,0)
raster.index(0,1)
raster.index(0,2)
raster.index(0,3)
raster.xy(0,0)
raster.xy(0,1)
import mpu
import geopy
pt1 = raster.xy(0,0)
pt2 = raster.xy(0,1)
geopy.distance
import geopy.distance
geopy.distance.vincenty(pt1, pt2).km
from geopy import distance
distance.vincenty(pt1, pt2)
distance.geodesic(pt1, pt2).m
distance.geodesic(pt1, pt2)
pt1
pt2
distance.distance((pt1, pt2)
distance.distance(pt1, pt2)
pt2
pt2 = pt2[::-1]
pt2
pt1 = pt1[::-1]
pt1
distance.distance(pt1, pt2)
distance.distance(pt1, pt2).m
distance.distance(pt1, pt2).km
distance.distance(pt1, pt2).miles
for i in range(10):
    distance.distance(raster.xy(0,i)[::-1], raster.xy(0,i+1)[::-1])
    
for i in range(10):
    distance.distance(raster.xy(0,i)[::-1], raster.xy(0,i+1)[::-1]).miles
    
zip_code_95444['geometry'].iloc[0].exterior.coords.xy
zip_code_95444['geometry'].iloc[0].exterior.coords
zip_code_95444.geometry.iloc[0].exterior.coords
zip_code_95444.geometry.exterior[0[
zip_code_95444.geometry.exterior[0]
zip_code_95444.geometry.exterior
zip_code_95444.geometry.iloc[0].exterior.coords
zip_code_95444.geometry.iloc[0].exterior.coords[0]
zip_code_95444.geometry.iloc[0].exterior.coords.xy
list(zip(*zip_code_95444.geometry.iloc[0].exterior.coords.xy))
zip_code_95444_coords = list(zip(*zip_code_95444.geometry.iloc[0].exterior.coords.xy))
zip_code_95444_coords
map(max, zip(*zip_code_95444_coords))
tuple(map(max, zip(*zip_code_95444_coords)))
tuple(map(min, zip(*zip_code_95444_coords)))
min_coord = tuple(map(min, zip(*zip_code_95444_coords)))
max_coord = tuple(map(min, zip(*zip_code_95444_coords)))
min_coord
max_coord
max_coord = tuple(map(max, zip(*zip_code_95444_coords)))
min_coord
max_coord
approx_coord_cluster = []
for i in range(10):
    distance.distance(raster.xy(0,i)[::-1], raster.xy(0,i+1)[::-1]).miles
    
raster.xy(0,i)[::-1]
raster.xy(0,1)[::-1]
i
raster.xy(0,0)
pt1 = raster.xy(0,1)[::-1]
pt1 = raster.xy(0,0)[::-1]
pt2 = raster.xy(0,2)[::-1]
pt1
pt2
pt1[0] - pt2[0]
pt1[1] - pt2[1]
pt2 = raster.xy(0,1)[::-1]
pt1 = raster.xy(0,0)[::-1]
pt3 = raster.xy(1,0)[::-1]
pt3
pt1
pt1[1] - pt2[1]
pt2[1] - pt1[1]
pt3[1] - pt1[1]
pt3[0] - pt1[0]
pt1[0] - pt3[0]
lat_long_increment = pt1[0] - pt3[0]
lat_long_increment
# get nearest raster pixel point to max and min coords of zip_code_95444
history():
def history():
    with open('python_history.py', 'w') as f:
import readline
def history():
    with open('python_history.py', 'w') as f:
        for i in range(readline.get_current_history_length()):
            f.write(readline.get_history_item(i+1))
            
        
    
history()
def history():
    with open('python_history.py', 'w') as f:
        for i in range(readline.get_current_history_length()):
            f.write(f'{readline.get_history_item(i+1)}\n')
            
        
    
history()
# get nearest raster pixel point to max and min coords of zip_code_95444
max_coord
min_coord
raster.index(max_coord)
raster.index(*max_coord)
raster_max_index = raster.index(*max_coord)
raster_min_index = raster.index(*min_coord)
raster_max_index
raster_min_index
raster.xy(*raster_max_index)
max_coord
raster.xy(*raster_min_index)
min_coord
distance.distance(raster.xy(*raster_min_index)[::-1], min_coord[::-1])
distance.distance(raster.xy(*raster_min_index)[::-1], min_coord[::-1]).miles
distance.distance(raster.xy(*raster_max_index)[::-1], max_coord[::-1]).miles
raster_min_zip_coord = raster.xy(*raster_min_index)
raster_max_zip_coord = raster.xy(*raster_max_index)
raster_min_zip_coord
raster_max_zip_coord
raster_min_zip_coord
raster_max_zip_coord
raster_max_zip_coord = raster_max_zip_coord[::-1]
raster_min_zip_coord = raster_min_zip_coord[::-1]
raster_min_zip_coord
raster_max_zip_coord
bounding_box_coords = [(raster_max_zip_coord[0], raster_min_zip_coord[1])]
raster_top_right_max_min_box
top_edge_max_min_box_len = distance.distance(raster_top_right_max_min_box, raster_max_zip_coord) 
top_edge_max_min_box_meters 
min_max_box_meters = distance.distance(raster_top_right_max_min_box, raster_max_zip_coord).meters 
top_edge_max_min_box_meters
top_edge_max_min_box_len = distance.distance(raster_top_right_max_min_box, raster_max_zip_coord) 
top_edge_max_min_box_len
top_edge_max_min_box_meters
top_edge_max_min_box_len = distance.distance(raster_top_right_max_min_box, raster_max_zip_coord).meters 
top_edge_max_min_box_len
bounding_box_width_meters = distance.distance(raster_top_right_max_min_box, raster_max_zip_coord).meters 
bounding_box_width_meters
bounding_box_height_meters = distance.distance(raster_top_right_max_min_box, raster_min_zip_coord).meters 
bounding_box_height_meters
raster_max_zip_coord
raster_min_zip_coord
def get_coords_bounding_box(min_coord, max_coord):
import numpy as np
np.arange(raster_min_zip_coord[0], raster_max_zip_coord[0])
dir()
lat_long_increment
np.arange(raster_min_zip_coord[0], raster_max_zip_coord[0], lat_long_increment)
def get_coords_bounding_box(min_coord, max_coord):
np.arange(raster_min_zip_coord[0], raster_max_zip_coord[0], lat_long_increment)
def get_coords_bounding_box(min_coord, max_coord):
lat_long_incrementnp.arange(raster_min_zip_coord[0], raster_max_zip_coord[0], lat_long_increment)
def get_coords_bounding_box(min_coord, max_coord):
    for lat in np.arange(raster_min_zip_coord[0], raster_max_zip_coord[0], lat_long_increment)
def get_coords_bounding_box(min_coord, max_coord):
    for lat in np.arange(raster_min_zip_coord[0], raster_max_zip_coord[0], lat_long_increment):
        for long in np.arange(raster_min_zip_coord[1], raster_max_zip_coord[1], lat_long_increment):
            print((lat, long))
            
        
    
get_coords_bounding_box(raster_min_zip_coord, raster_max_zip_coord)
def get_coords_bounding_box(min_coord, max_coord):
def get_coords_bounding_box
get_coords_bounding_box
def get_coords_bounding_box(min_coord, max_coord):
    lat_list = np.arange(raster_min_zip_coord[0], raster_max_zip_coord[0], lat_long_increment)
    long_list = np.arange(raster_min_zip_coord[1], raster_max_zip_coord[1], lat_long_increment)
    return [list(zip(x, long_list)) for x in itertools.permutations(lat_list, len(long_list))]
    
get_coords_bounding_box(raster_min_zip_coord, raster_max_zip_coord)
import itertools.permutations
from itertools import permutations
import itertools
get_coords_bounding_box(raster_min_zip_coord, raster_max_zip_coord)
history()
zip_contain_coords = get_coords_bounding_box(raster_min_zip_coord, raster_max_zip_coord)
zip_contain_coords
zip_contain_coords = [coord[::-1] for coord in zip_contain_coords]
zip_contain_coords
def get_coords_bounding_box(min_coord, max_coord):
    lat_list = np.arange(raster_min_zip_coord[0], raster_max_zip_coord[0], lat_long_increment)
    long_list = np.arange(raster_min_zip_coord[1], raster_max_zip_coord[1], lat_long_increment)
    return [list(zip(x, long_list)) for x in itertools.permutations(lat_list, len(long_list))]
    
np.arange(raster_min_zip_coord[0], raster_max_zip_coord[0], lat_long_increment)
list(np.arange(raster_min_zip_coord[0], raster_max_zip_coord[0], lat_long_increment))
def get_coords_bounding_box(min_coord, max_coord):
    lat_list = np.arange(raster_min_zip_coord[0], raster_max_zip_coord[0], lat_long_increment)
    lat_list = list(np.arange(raster_min_zip_coord[0], raster_max_zip_coord[0], lat_long_increment))
    long_list = list(np.arange(raster_min_zip_coord[1], raster_max_zip_coord[1], lat_long_increment))
    return [list(zip(x, long_list)) for x in itertools.permutations(lat_list, len(long_list))]
    
zip_contain_coords = get_coords_bounding_box(raster_min_zip_coord, raster_max_zip_coord)
zip_contain_coords
zip_contain_coords = get_coords_bounding_box(raster_min_zip_coord, raster_max_zip_coord)
zip_contain_coords 
get_coords_bounding_box(raster_min_zip_coord, raster_max_zip_coord)
raster_max_zip_coord
raster_min_zip_coord
lat_list = list(np.arange(raster_min_zip_coord[0], raster_max_zip_coord[0], lat_long_increment))
long_list = list(np.arange(raster_min_zip_coord[1], raster_max_zip_coord[1], lat_long_increment))
lat_list
long_list
[list(zip(x, long_list)) for x in itertools.permutations(lat_list, len(long_list))]
list(itertools.product(long_list, lat_list))
long_list
lat_list
history()
