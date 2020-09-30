from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome()
productName = []
productPrice = []
productRating = []

driver.get("https://www.americanas.com.br/categoria/celulares-e-smartphones/smartphone")

pageContent = driver.page_source

soup = BeautifulSoup(pageContent, features='lxml')

for item in soup.findAll('div', attrs={'class':'row product-grid no-gutters main-grid'}):
  for product in item.findAll('div', attrs={'class': 'product-grid-item ColUI-gjy0oc-0 hFbhrr ViewUI-sc-1ijittn-6 iXIDWU'}):
    name = product.find('h2')
    price = product.find('span', attrs={'class': 'PriceUI-bwhjk3-11 cmTHwB PriceUI-sc-1q8ynzz-0 dHyYVS TextUI-sc-12tokcy-0 bLZSPZ'})
    rating = product.find('span', attrs={'class': 'Quantity-sc-1fg2071-3 RsSwi TextUI-sc-12tokcy-0 kzcXGa'})
    
    if(name and price and rating):
      productName.append(name.text)
      productPrice.append(price.text)
      productRating.append(rating.text)

df = pd.DataFrame({'Product Name': productName, 'Price': productPrice, 'rating': productRating})
df.to_csv('products.csv', index=False, encoding='utf-8')
