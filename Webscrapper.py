from urllib.request import urlopen 
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd

#Set page URL
url = 'https://fr.investing.com/indices/us-spx-500-technical'
#User request (Some site forbid use of bot so its required to impersonate a user)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
req = urllib.request.Request(url, headers=headers)
try:
    page_hw = urllib.request.urlopen(req)
    # Continue with your code here
except urllib.error.HTTPError as e:
    print(f'HTTP Error {e.code}: {e.reason}')
except urllib.error.URLError as e:
    print(f'URL Error: {e.reason}')

soup = BeautifulSoup(page_hw, 'html.parser')

#Get all data needed
indicator = soup.findAll(name='td', attrs={'class': 'datatable_cell__LJp3C !py-3 w-full !border-t-[#e6e9eb]'})
indicator_txt = [td.get_text(strip=True) for td in indicator]

value = soup.findAll(name='td', attrs={'class': 'datatable_cell__LJp3C !py-3 ltr:!text-right !border-t-[#e6e9eb] rtl:soft-ltr'})
value_txt = [td.get_text(strip=True) for td in value]

position = soup.findAll(name='td', attrs={'class': 'datatable_cell__LJp3C datatable_cell--up__hIuZF datatable_cell--bold__5MJH6 !py-3 ltr:!text-right !border-t-[#e6e9eb]'})
position_txt = [td.get_text(strip=True) for td in position]

#DataFrame Creation
df = pd.DataFrame(list(zip(indicator_txt, value_txt, position_txt)), columns=['Indicateur', 'Valeur', 'Type de Position'])

#Set save PATH
df.to_csv('C:/Users/loiic/Desktop/code/Bot WebScrapping/result.csv')
