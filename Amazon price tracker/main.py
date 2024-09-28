import requests
from bs4 import BeautifulSoup
import smtplib

EMAIL = "XXXX@gmail.com"
PASSWORD = "XXXXX"
URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
header = {
 "User-Agent": "XXXXXXX",
 "Accept-Language": "en-US,en;q=0.9,en-IN;q=0.8"
}
response = requests.get(URL, headers=header)
response_text = response.text
soup = BeautifulSoup(response_text, "html.parser")
price_tag = soup.find(name="span", class_="aok-offscreen")
price = price_tag.getText().split("$")
Floating_price = float(price[1])

Product_title = soup.find(name='span', id="productTitle")
title = Product_title.get_text().split(",")
Product_name = title[0]
if Floating_price < 100:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=EMAIL, password=PASSWORD)
    msg = (f"subject:Its your day to buy\n\n Your desired product {Product_name}is at buying cost {Floating_price}"
           f"\n Go and buy {URL}")
    connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg=msg)
