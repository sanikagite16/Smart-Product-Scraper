from flask import Flask, render_template, send_file
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
            best_rating=0,
            electronics_count=0,
            beauty_count=0,
            groceries_count=0,
            furniture_count=0
        )

    electronics_count = len(
        [p for p in products if p["category"] == "Electronics"]
    )

    beauty_count = len(
        [p for p in products if p["category"] == "Beauty"]
    )

    groceries_count = len(
        [p for p in products if p["category"] == "Groceries"]
    )

    furniture_count = len(
        [p for p in products if p["category"] == "Furniture"]
    )

    prices = [
        int(str(p["price"]).replace("₹", ""))
        for p in products
    ]

    ratings = [
        float(p["rating"])
        for p in products
    ]

    return render_template(
        "index.html",
        products=products,
        total_products=len(products),
        highest=max(prices),
        lowest=min(prices),
        best_rating=max(ratings),
        electronics_count=electronics_count,
        beauty_count=beauty_count,
        groceries_count=groceries_count,
        furniture_count=furniture_count
    )

@app.route("/products.csv")
def download_csv():

    return send_file(
        "products.csv",
        as_attachment=True
    )

if __name__ == "__main__":
    app.run(debug=True)