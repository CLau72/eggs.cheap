from flask import Flask, render_template
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import matplotlib.pyplot as plt
import io
import os
import base64

load_dotenv(dotenv_path=".env")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URI")
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
        prices.append(value.price)


    # Create a plot
    plt.figure(figsize=(8, 5))
    plt.xlabel("Date")
    plt.ylabel("Price/Dozen (USD)")
    if prices[-1] >= BIDEN_PRICE:
        plt.title("No.",fontsize=30)
    else:
        plt.title("YES!",fontsize=30)

    plt.axhline(y=BIDEN_PRICE, color='b', linestyle="--", label="Biden Final Price")
    plt.plot(dates,prices, color="r", label="Current Price")
    plt.legend(loc="lower right")
    plt.annotate(f"${prices[-1]}",xy=(dates[-1], prices[-1]),
    textcoords='offset points', ha='center', va='center'
    )
    plt.ylim(bottom=0, top=8)

    # Save the plot to a BytesIO object
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Encode the BytesIO object in base64
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')

    # Render the plot in an HTML template
    return render_template('index.html', plot_url=plot_url)

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
