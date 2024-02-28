import requests
from bs4 import BeautifulSoup as bs
import smtplib

URL = "https://www.amazon.in/9500-15-6-inch-i7-10750H-NVIDIA1650-Graphics/dp/B08BZPRWR5/ref=sr_1_4?dchild=1&keywords=Dell+XPS+15&qid=1602254565&sr=8-4"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
}


def check_price():
    """Check Price of Product""" 
    page = requests.get(URL, headers=headers)
    soup = bs(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    price.replace("₹", "")
    price.replace(",", "")
    price.replace(" ", "")
    price.replace("\\xa;", "")
    converted_price = float(price[0:5])
    if (converted_price < 2000000.00):
        send_mail()

    print(converted_price)


def send_mail():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("sachinsamurai@gmail.com", "Baahubali")
    subject = "Price went down for DELL XPS 15"
    body = ("Check it out: https://www.amazon.de/Dell-Generation-i7-10750H-N18P-G62-DDR4-2933MHz/dp/B088TWQ1V8/ref=sr_1_1?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1QODNEAOK4F7R&dchild=1&keywords=dell+xps+15&qid=1602067797&quartzVehicle=93-295&replacementKeywords=dell+xps&sprefix=Dell+XPS+%2Caps%2C281&sr=8-1")

    msg = f"Subject: {subject} \n\n {body}"
    server.sendmail(
        "sachinsamurai@gmail.com",
        "sachinsamurai@gmail.com",
        msg
    )
    print("Email sent")
    server.quit()


check_price()
