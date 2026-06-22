import requests
import csv

def scrape_products():

    url = "https://fakestoreapi.com/products"

    response = requests.get(url, timeout=10)

if response.status_code != 200:
    return []

products = response.json()

    product_list = []

    for product in products:

        category = product["category"]

        if category == "men's clothing":
            category = "Fashion"

        if category == "women's clothing":
            category = "Fashion"

        if category == "jewelery":
            category = "Jewelry"

        product_list.append({

            "name": product["title"],
            "price": f"₹{round(product['price'] * 85)}",
            "category": category,
            "rating": product["rating"]["rate"],
            "image": product["image"]

        })

    with open(
        "products.csv",
        "w",
        newline="",
        encoding="utf-8-sig"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "Name",
            "Price",
            "Category",
            "Rating"
        ])

        for product in product_list:

            writer.writerow([
                product["name"],
                product["price"],
                product["category"],
                product["rating"]
            ])

    return product_list