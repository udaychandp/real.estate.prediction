import requests
from bs4 import BeautifulSoup
import csv
import sys


url = 'https://www.magicbricks.com/property-for-sale/residential-real-estate?bedroom=2,3&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa&cityName=Hyderabad'
# url = sys.argv[1]
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html')
# print(soup)
property_listings = soup.find_all('div',class_='mb-srp__card__price')
for_title = soup.find_all('h2',class_='mb-srp__card--title')
# print(property_listings)
# print(property_listings[0].find('div', class_='mb-srp__card__price--amount').text.strip())

csv_filename = 'magicbricks_data.csv'

with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:

    csv_writer = csv.writer(csv_file)
    headers = ['Property Title','BHK' ,'Price','area' ,'Location']
    csv_writer.writerow(headers)
    for x in range(len(for_title)):
        try: 
            title = for_title[x].get('title')
            type = title.split()[0]
            price1 = property_listings[x].find('div', class_='mb-srp__card__price--amount').text.strip()
            
            if price1.split()[-1] =='Cr':
                price = eval(price1.split()[0][1:])*10000000
            else:
                price = eval(price1.split()[0][1:])*100000
            area1 = property_listings[x].find('div', class_='mb-srp__card__price--size').text.strip()
            area = area1.split()[0][1:]
            location = for_title[x].get('title').split()[-1]
        except AttributeError:
            area = 'NaN'
            
        csv_writer.writerow([title, type,price,area ,location])