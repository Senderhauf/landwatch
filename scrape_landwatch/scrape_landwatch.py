import requests
from bs4 import BeautifulSoup

def getListingLinkDict(link_html):
   inner_text = link_html.get_text()
   location = None
   price = 0
   index_acres = inner_text.index('Acres')
   acres = inner_text[:index_acres].strip()
   loc_price_arr = inner_text[index_acres::].split('$')

   if len(loc_price_arr) == 2:
      location = loc_price_arr[0].strip()
      price = loc_price_arr[1].replace(',', '').strip()

   return {
      'route': link_html['href'],
      'acres': acres,
      'location': location,
      'price': int(price)
   }

def main():
   BASE_URL = 'https://www.landwatch.com/default.aspx?'
   min_acre = 5
   max_acre = 40
   min_price = 5000
   max_price = 20000
   headers = {'User-Agent': 'Mozilla/5.0 (X11: Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'}

   for i in range(25, 84):
      request_url = f'{BASE_URL}ct=r&type=5,{i}&r.PSIZ={min_acre},{max_acre}&pn={min_price}&px={max_price}'
      req = requests.get(request_url, headers=headers)
      soup = BeautifulSoup(req.text, 'html.parser')

      links = soup.find_all('a', {'data-action': 'resultsTitle'})
      link_dict = [ getListingLinkDict(link) for link in links]
      if len(link_dict):
         print(f'len(link_dict): {len(link_dict)}')
         print(link_dict[0])
         print()

if __name__ =='__main__':
    main()
