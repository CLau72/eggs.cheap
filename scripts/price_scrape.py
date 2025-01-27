import requests
from bs4 import BeautifulSoup
from datetime import date
from sqlalchemy import create_engine, Column, Numeric, Date
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
import os

# URL to scrape
URL = "https://tradingeconomics.com/commodity/eggs-us"

# .env file load
load_dotenv(dotenv_path='../.env')
database_url = os.getenv('DATABASE_URI')

print(database_url)

# DB setup
engine = create_engine(database_url)
Base = declarative_base()

class Price(Base):
    __tablename__ = 'prices'
    price = Column(Numeric(10,2))
    date = Column(Date, primary_key=True)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Scrape the page
def price_scrape(url=URL):
    page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(page.content, "html.parser")

    # Grab table with the price data
    # After grabbing the table, the "Actual" price is in the 2nd td tag
    results = soup.find(id="ctl00_ContentPlaceHolder1_ctl00_ctl02_Panel1")
    prices = []
    for data in results.find_all("td"):
        prices.append(data.get_text())

    current_egg_price = float(prices[1])
    return current_egg_price


price = Price(price=price_scrape(), date=date.today())
try:
    session.add(price)
    session.commit()
    print(f"New data: ${price.price}, {price.date} added successfully")
except:
    print("Failed to add new data")
