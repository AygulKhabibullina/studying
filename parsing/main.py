import requests
from bs4 import BeautifulSoup
import csv

CSV = 'flats.csv'
HOST = 'https://www.domofond.ru'
URL = 'https://www.domofond.ru/prodazha-kvartiry-moskva-c3584'

HEADERS = {
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
}

def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params, timeout=20)
    return r

def get_picture(item):
    html = get_html(item)
    soup = BeautifulSoup(html.text, 'html.parser')
    picture = soup.find('img', class_='gallery__image___2xHLz').get("src"),
    return picture

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def configure_driver():
    # Add additional Options to the webdriver
    chrome_options = Options()
    # add the argument and make the browser Headless.
    chrome_options.add_argument("--headless")
    # Instantiate the Webdriver: Mention the executable path of the webdriver you have downloaded
    driver = webdriver.Chrome(executable_path="./chromedriver.exe", options = chrome_options)
    return driver


def getFlatInfo(driver, link_item):
    # Step 1: Go to pluralsight.com, category section with selected search keyword
    driver.get(link_item)
    # Step 2: Create a parse tree of page sources after searching
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.close()
    return soup

def parsePicture(link_item):
    driver = configure_driver()
    soup = getFlatInfo(driver, link_item)
    return soup.select_one("img.gallery__image___2xHLz").attrs.get("src")

def write_metro(item):
    metro = item.find('span', class_='metro__metroName___wZUoM')
    if metro is None:
        return ''
    else:
        return metro.get_text()

def get_content(html):
    soup = BeautifulSoup(html.text, 'html.parser')
    items = soup.find_all('a',class_='long-item-card__item___ubItG')
    flats = []
    for item in items:
        flatLink = HOST + item.attrs.get("href")
        picture = parsePicture(flatLink)
        flats.append(
            {
                'title': item.find('div',class_='long-item-card__informationHeaderRight___3bkKw').get_text(),
                'price': item.find('span',class_='long-item-card__price___3A6JF').get_text(),
                'price_per_sqr_meter': item.find('div',class_='additional-price-info__additionalPriceInfo___lBqNv').get_text(),
                'address': item.find('span',class_='long-item-card__address___PVI5p').get_text(),
                'description': item.find('div', 'description__descriptionBlock___3KWc1').get_text(),
                'metro': write_metro(item),
                'picture': picture,
                'link': flatLink
            }
        )
    return flats

def save_csv(path, items):
    with open(path, 'w', newline='', encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Квартира', 'Цена', 'Цена за кв. м.', 'Адрес', 'Описание', 'Метро', 'Фото' 'Ссылка'])
        for item in items:
            writer.writerow([item['title'], item['price'], item['price_per_sqr_meter'], item['address'], item['description'], item['metro'], item['picture'], item['link']])

def parse_pages():
    pagination = int(input('Сколько страниц парсим: ').strip())
    print(pagination)
    html = get_html(URL)
    if html.status_code ==200:
        flats = []
        for page in range(1, pagination + 1):
            print(f'Парсинг страницы: {page}')
            html = get_html(URL, params={'Page': page})
            flats.extend(get_content(html))
            save_csv(CSV, flats)
    else:
        print('Код возврата не 200')

parse_pages()
#html = get_html(URL)
#flats = get_content(html)
#print(flats)
#save_csv(CSV, flats)