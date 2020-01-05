import requests
from bs4 import BeautifulSoup as BS
import csv


def load_soup(url):
    response = requests.get(url)
    response.raise_for_status()
    return BS(response.text, 'html.parser')

domain = 'https://volby.cz/pls/ps2017nss/'
district_links = []
header_url = 'https://www.volby.cz/pls/ps2017nss/ps2?xjazyk=CZ'

def municipality_links():
    soup = load_soup('https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ')
    print('Loading soup https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ')
    for href in soup.find_all('a', href=True):
        if 'ps32' in href['href']:
            district_links.append(domain+href['href'])
    municipality_links = []
    for link in district_links:
        response = requests.get(link)
        soup = BS(response.content, 'html.parser')
        for td in soup.find_all('td',{'class':'cislo'}):
            for municipality in td:
                city = municipality.get_text()
                city_link = (domain+municipality['href'])
                municipality_links.append([city, city_link])
    return municipality_links

def scrape_data_header(url):
    soup = load_soup(url)
    header_row = ['code', 'location', 'registered', 'envelopes', 'valid']

    election_results_table1 = soup.find_all('table', class_="table")[1]
    election_results_table2 = soup.find_all('table', class_="table")[2]

    for element in election_results_table1.find_all('tr'):
        cell = element.find('td', headers="t1sa1 t1sb2")
        if cell != None:
            header_row.append(cell.get_text())

    for element2 in election_results_table2.find_all('tr'):
        cell = element2.find('td', headers="t2sa1 t2sb2")
        if cell != None:
            header_row.append(cell.get_text())
    return header_row

def scrape_data_row(code, url):
    soup = load_soup(url)

    election_results_table1 = soup.find_all('table', class_="table")[1]
    election_results_table2 = soup.find_all('table', class_="table")[2]

    for header in soup.find_all(class_="topline", id="publikace"):   #scraping city name
        city = header.find_all('h3')[-1].get_text()
        city = city.replace('\n', '')
        city = city.replace('Obec: ', '')

    registered = soup.find(id='ps311_t1').find('td', class_="cislo", headers="sa2").get_text()
    envelopes = soup.find(id='ps311_t1').find('td', class_="cislo", headers="sa3").get_text()
    valid = soup.find(id='ps311_t1').find('td', class_="cislo", headers="sa6").get_text()
    row_dict = {}
    row = [code, city, str(registered).replace('\xa0',''), str(envelopes).replace('\xa0',''), str(valid).replace('\xa0','')]

    for element in election_results_table1.find_all('tr'):
        cell = element.find('td', class_="cislo", headers="t1sa2 t1sb3")
        party_number = element.find('td', class_="cislo", headers="t1sa1 t1sb1")
        if party_number != None:
            row_dict[party_number.get_text()] = cell.get_text().replace('\xa0','')
            # row.append(cell.get_text().replace('\xa0',''))

    for element2 in election_results_table2.find_all('tr'):
        cell2 = element2.find('td', class_="cislo", headers="t2sa2 t2sb3")
        party_number2 = element2.find('td', class_="cislo", headers="t2sa1 t2sb1")
        if party_number2 != None:
            row_dict[party_number2.get_text()] = cell2.get_text().replace('\xa0','')
            # row.append(cell2.get_text().replace('\xa0',''))
    for i in range(1, 32):
        i = str(i)
        if i in row_dict:
             row.append(row_dict[i])
        else:
            row.append('0')
    return row

def csv_writer(data):
    with open('volby_2017.csv', 'wt', newline='') as file:
        writer = csv.writer(file, delimiter=';', quotechar=' ')
        for row in data:
            writer.writerow(row)
def main():
    all_data = []
    all_data.append(scrape_data_header(header_url))
    for url in municipality_links():
        print('Scraping link:', url)
        all_data.append(scrape_data_row(url[0], url[1]))
    csv_writer(all_data)

main()
