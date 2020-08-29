import requests
from bs4 import BeautifulSoup
import random

def setup():
    BASE_URL = 'https://www.landandfarm.com/search/'
    min_acre = 5
    max_acre = 60
    min_price = 5000
    max_price = 40000

    STATES_LIST = [
        # ('Alabama', 'AL')
        # ('Alaska', 'AK')
        # ('Arizona', 'AZ')
        # ('Arkansas', 'AR')
        # ('California', 'CA')
        # ('Colorado', 'CO')
        # ('Connecticut', 'CT')
        # ('Delaware', 'DE')
        # ('Florida', 'FL')
        # ('Georgia', 'GA')
        # ('Hawaii', 'HI')
        # ('Idaho', 'ID')
        # ('Illinois', 'IL')
        # ('Indiana', 'IN')
        # ('Iowa', 'IA')
        # ('Kansas', 'KS')
        # ('Kentucky', 'KY')
        # ('Louisiana', 'LA')
        # ('Maine', 'ME')
        # ('Maryland', 'MD')
        # ('Massachusetts', 'MA')
        # ('Michigan', 'MI')
        # ('Minnesota', 'MN')
        # ('Mississippi', 'MS')
        # ('Missouri', 'MO')
        # ('Montana', 'MT')
        # ('Nebraska', 'NE')
        # ('Nevada', 'NV')
        # ('New Hampshire', 'NH')
        # ('New Jersey', 'NJ')
        # ('New Mexico', 'NM')
        # ('New York', 'NY')
        # ('North Carolina', 'NC')
        # ('North Dakota', 'ND')
        # ('Ohio', 'OH')
        # ('Oklahoma', 'OK')
        # ('Oregon', 'OR')
        # ('Pennsylvania', 'PA')
        # ('Rhode Island', 'RI')
        # ('South Carolina', 'SC')
        # ('South Dakota', 'SD')
        ('Tennessee', 'TN')
        # ('Texas', 'TX')
        # ('Utah', 'UT')
        # ('Vermont', 'VT')
        # ('Virginia', 'VA')
        # ('Washington', 'WA')
        # ('West Virginia', 'WV')
        # ('Wisconsin', 'WI')
        # ('Wyoming', 'WY')
    ]

    STATES_ABREVIATION_LIST = [
        'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL', 'GA',
        'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN',
        'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK',
        'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'
    ]


    USER_AGENT_LIST = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:79.0) Gecko/20100101 Firefox/79.0',
        'Mozilla/5.0 (X11; Linux i686; rv:79.0) Gecko/20100101 Firefox/79.0',
        'Mozilla/5.0 (Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0',
        'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:79.0) Gecko/20100101 Firefox/79.0',
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0',
        'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    ]
    
    for state in STATES_LIST:
        # 'https://www.landandfarm.com/search/Tennessee-land-for-sale/?MinAcreage=10&MaxAcreage=60&MinPrice=5000&MaxPrice=40000'
        request_url = f'{BASE_URL}{state[0]}-land-for-sale/?MinAcreage={min_acre}&MaxAcreage={max_acre}&MinPrice={min_price}&MaxPrice={max_price}'
        request_url = "https://www.landandfarm.com/search/Arizona-land-for-sale/?MinAcreage=10&MaxAcreage=10&MinPrice=14999&MaxPrice=15000"
        # get random user-agent
        headers = {'User-Agent': random.choice(USER_AGENT_LIST)}
        res = requests.get(request_url, headers=headers)
        if res.status_code == 200:
            print(request_url)
            with open('debug.html', 'w') as debugHtml:
                debugHtml.write(res.text);
            soup = BeautifulSoup(res.text, 'html.parser')
            return soup
            # if not soup.findAll(text='No Results Found For Your Current Search'):
            #     results_el = soup.find('div', {'id': 'searchResultsGrid'})
            #     property_card_el_list = results_el.find_all('article', {'class': 'property-card'})
            #     property_info_list = [getPropertyInfo(prop_el, row[1], row[0]) for prop_el in property_card_el_list]
            #     for prop_info in property_info_list:
            #         insertListingDB(prop_info)

        else:
            print(f'Request not 200: {request_url}')
            print.error(res)
