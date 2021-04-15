import requests
import bs4


def is_ascii(s):
    try:
        s.decode('ascii')
        return True
    except UnicodeDecodeError:
        return False


page = requests.get(
    'https://www.dell.com/en-us/shop/dell-laptops/new-xps-15-laptop/spd/xps-15-9500-laptop/xn9500ecxns')
soup = bs4.BeautifulSoup(page.content, 'html.parser')

prices = soup.find(
    class_='cf-dell-price').text.encode('unicode_escape').decode()

price = prices.split(" ")[12]

prices[12].replace("$", "")
prices[12].replace(",", "")

print(prices[12])
