from attr import attr
import requests
from bs4 import BeautifulSoup

url='https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3DApple&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIlNob3AgTm93Il0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&otracker=clp_metro_expandable_7_3.metroExpandable.METRO_EXPANDABLE_Shop%2BNow_mobile-phones-store_92RED14GXPXF_wp2&fm=neo%2Fmerchandising&iid=M_be92206f-4afa-4ac5-aff4-964bf716d2c7_3.92RED14GXPXF&ppt=hp&ppn=homepage&ssid=mrrytx7040dxqkn41658205782705'
res=requests.get(url)
# print(res)
soup=BeautifulSoup(res.content,'html.parser')
products=soup.findAll('a',attrs={'class':'_1fQZEK'})

for product in products:
    name=product.find('div',attrs={'class':'_4rR01T'}).text
    print(name)
