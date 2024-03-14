import requests
import lxml
from bs4 import BeautifulSoup
from mail import Mail

URL = "https://www.amazon.in/CRAZYMONK-Yeager-Freedom-Oversized-T-Shirt/dp/B0CBJZY713/?_encoding=UTF8&ref_=pd_gw_ci_mcx_mr_hp_atf_m"


response = requests.get(
    url=URL,
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Accept-Language":"en-US,en;q=0.7"
    })
contents = response.text

soup = BeautifulSoup(contents,"lxml")

price = soup.find(class_= "a-price-whole").getText()

title_of_product = soup.find(id="productTitle").getText().strip()

if int(price) < 300:
    mail = Mail(int(price),title_of_product)
    mail.send_myself_mail()

