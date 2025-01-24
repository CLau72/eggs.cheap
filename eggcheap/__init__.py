from flask import Flask, render_template
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

BIDEN_PRICE = 6.12

@app.route('/')
def plot():

    # Data
    dates = ["2025-01-20","2025-01-21","2025-01-22","2025-01-23"]
    prices = [6.12,6.55,6.55,6.55]

    # Create a plot
    plt.figure(figsize=(8, 5))
    plt.xlabel("Date")
    plt.ylabel("Price/Dozen (USD)")
    if prices[-1] >= BIDEN_PRICE:
        plt.title("No.",fontsize=30)
    else:
        plt.title("YES!",fontsize=30)

    plt.axhline(y=BIDEN_PRICE, color='b', linestyle="--", label="Biden Final Price")
    plt.plot(dates,prices, color="r")
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

if __name__ == '__main__':
    app.run(debug=True)
