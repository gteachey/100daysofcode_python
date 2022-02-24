import requests
from smtplib import SMTP
from bs4 import BeautifulSoup

PRICE_LIMIT = 100.00
HEADERS = {
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    # 'Host': 'myhttpheader.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'
}

url = 'https://www.amazon.com/Instant-Pot-Plus-Programmable-Sterilizer/dp/B075CYMYK6/ref=dp_fod_1?pd_rd_i=B075CYMYK6&psc=1'
response = requests.get(url=url, headers=HEADERS)
response.raise_for_status()
soup = BeautifulSoup(response.text, features="lxml")
# print(soup.prettify())
# with open("webpage.html", "w", encoding='utf-8') as file:
#     file.write(str(soup))
# with open("webpage.html", "r", encoding='utf-8') as file:
#     soup = BeautifulSoup(file.read(), features="lxml")

attrs = {
    'id': "twister-plus-price-data-price"
}

price_grabber = soup.find(name="input", attrs=attrs)
price = price_grabber['value']

attrs = {
    'id': "productTitle"
}
product_title = soup.find(name="span", attrs=attrs)
product_name = product_title.getText().strip()
print(product_name)

if float(price) < PRICE_LIMIT:
    smtp_provider = 'smtp.gmail.com'
    smtp_user = 'gt100daysofcode'
    smtp_send_user = 'gteachey@outlook.com'
    smtp_password = 'T..h7RP#tz;G[t27bC,y'
    message = f"To: {smtp_send_user}\n" \
              f"Subject: Price Drop Alert!\n\n" \
              f"Your Item:\n{product_name}\n\b" \
              f"Is now ${price}!\n\n" \
              f"Go get that plasti-cash and achieve the American Dream!!!\n{url}".encode("utf-8").strip()

    with SMTP(smtp_provider) as smtp_mailer:
        smtp_mailer.starttls()
        smtp_mailer.login(smtp_user, smtp_password)
        smtp_mailer.sendmail(from_addr=smtp_user, to_addrs=smtp_send_user, msg=message)
