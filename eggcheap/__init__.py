from flask import Flask, render_template
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
import os

load_dotenv(dotenv_path=".env")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URI")
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle' : 280} 
db = SQLAlchemy(app)

class Prices(db.Model):
    date = db.Column(db.Date, primary_key = True)
    price = db.Column(db.Numeric(10,2), nullable = False)

BIDEN_PRICE = 6.12

@app.route('/')
def plot():

    dates = []
    prices = []

    # Data
    price_data = Prices.query.order_by(Prices.date).all()
    for value in price_data:
        dates.append(value.date.strftime("%Y-%m-%d"))
        prices.append("{:.2f}".format(float(value.price)))

    # Render the plot in an HTML template
    return render_template('index.html', labels=dates, values=prices)

@app.route('/dbtest')
def dbtest():
    price_array = []
    date_array = []

    prices = Prices.query.order_by(Prices.date).all()
    for price in prices:
        price_array.append(price.price)
        date_array.append(price.date)
    return price_array

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
