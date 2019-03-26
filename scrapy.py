import requests
from bs4 import BeautifulSoup

url = 'https://list.tmall.com/search_product.htm?spm=a222t.7794920.fsnav.8.6fb839edjCElIh&cat=50924003&acm=lb-zebra-24139-328537.1003.4.455785&scm=1003.4.lb-zebra-24139-328537.OTHER_14458839888552_455785'
html = requests.get(url).content
soup = BeautifulSoup(html, 'lxml')
for product_list in soup.findAll('div', 'product'):
    product_title = product_list.find('p', 'productTitle').a.text
    print(product_title)

    product_price = product_list.find('p', 'productPrice').em.text
    print(product_price)

    product_status = product_list.find('p', 'productStatus').text
    print(product_status)
