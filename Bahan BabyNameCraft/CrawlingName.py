import requests
from bs4 import BeautifulSoup
import csv
from tqdm import tqdm
import time

# Inisialisasi URL dan nomor halaman
url_base = 'https://quranicnames.com/boys/page/'
page_num = 1

# Inisialisasi file CSV untuk URL dan detail data
with open('list_url_boys.csv', 'w', newline='', encoding='utf-8') as list_url_csv, \
     open('detail_data_boys.csv', 'w', newline='', encoding='utf-8') as detail_data_csv:
    
    list_url_writer = csv.writer(list_url_csv)
    list_url_writer.writerow(['URL'])
    
    detail_data_writer = csv.writer(detail_data_csv)
    detail_data_writer.writerow(['Name', 'Arabic Name', 'Variant', 'Content'])
    
    urls_list = []
    
    # Loop untuk mengambil URL dari setiap halaman
    while True:
        url = url_base + str(page_num) + '/'
        response = requests.get(url)
        
        if response.status_code != 200:
            break
        
        soup = BeautifulSoup(response.content, 'html.parser')
        name_divs = soup.find_all('div', {'class': 'post'})
        
        for div in name_divs:
            name_link = div.find('a', {'class': 'boys'})
            if name_link:
                url = name_link['href']
                urls_list.append(url)
                list_url_writer.writerow([url])
        
        page_num += 1
        time.sleep(1)  # Penundaan untuk menghindari batasan server

    # Proses untuk mengambil detail dari setiap URL yang dikumpulkan
    pbar = tqdm(total=len(urls_list))
    for url in urls_list:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            name_elem = soup.find('h1', {'class': 'entry-title name'})
            name = name_elem.text.strip() if name_elem else 'N/A'
            arabic_name_elem = soup.find('td', {'class': 'arspelling'})
            arabic_name = arabic_name_elem.text.strip() if arabic_name_elem else 'N/A'
            variant_list = soup.find_all('div', {'class': 'variant'})
            variant = ', '.join([v.text.strip() for v in variant_list]) if variant_list else 'N/A'
            name_details_div = soup.find('div', {'id': 'name_details'})
            content_elem = name_details_div.find('p') if name_details_div else None
            content = content_elem.text.strip() if content_elem else 'N/A'
            
            detail_data_writer.writerow([name, arabic_name, variant, content])
        
        pbar.update(1)
        time.sleep(0.5)  # Penundaan untuk menghindari batasan server

    pbar.close()
