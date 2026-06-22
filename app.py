from flask import Flask, render_template
from flask import send_file
from scraper import scrape_products

app = Flask(__name__)

@app.route("/")
def home():

    products = scrape_products()

    if not products:
        return render_template(
            "index.html",
            products=[],
            highest=0,
            lowest=0,
            electronics_count=0,
            fashion_count=0,
            jewelry_count=0
        )

    electronics_count = len(
        [p for p in products if p["category"] == "electronics"]
    )

    fashion_count = len(
        [p for p in products if p["category"] == "Fashion"]
    )

    jewelry_count = len(
        [p for p in products if p["category"] == "Jewelry"]
    )

    prices = [
        int(p["price"].replace("₹", ""))
        for p in products
    ]

    return render_template(
        "index.html",
        products=products,
        highest=max(prices),
        lowest=min(prices),
        electronics_count=electronics_count,
        fashion_count=fashion_count,
        jewelry_count=jewelry_count
    )

@app.route("/products.csv")
def download_csv():

    return send_file(
        "products.csv",
        as_attachment=True
    )

if __name__ == "__main__":
    app.run(debug=True)