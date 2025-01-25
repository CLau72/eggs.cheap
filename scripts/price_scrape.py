import requests
from bs4 import BeautifulSoup

# Scrape the page
URL = "https://tradingeconomics.com/commodity/eggs-us"
page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(page.content, "html.parser")

# Grab table with the price data
results = soup.find(id="ctl00_ContentPlaceHolder1_ctl00_ctl02_Panel1")
prices = []
for data in results.find_all("td"):
    prices.append(data.get_text())

current_egg_price = float(prices[1])
