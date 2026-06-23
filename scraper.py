import requests
import csv

def scrape_products():

    try:

        all_products = []

        urls = [
            "https://dummyjson.com/products/category/smartphones",
            "https://dummyjson.com/products/category/laptops",
            "https://dummyjson.com/products/category/beauty",
            "https://dummyjson.com/products/category/groceries",
            "https://dummyjson.com/products/category/furniture"
        ]

        for url in urls:

            response = requests.get(
                url,
                timeout=15,
                headers={
                    "User-Agent": "Mozilla/5.0"
                }
            )

            response.raise_for_status()

            data = response.json()["products"]

            all_products.extend(data)

    except Exception as e:

        print("API ERROR:", e)
        return []

    product_list = []

    for product in all_products:

        category = product["category"]

        if category in [
            "smartphones",
            "laptops"
        ]:
            category = "Electronics"

        elif category == "beauty":
            category = "Beauty"

        elif category == "groceries":
            category = "Groceries"

        elif category == "furniture":
            category = "Furniture"

        product_list.append({

            "name": product["title"],
            "price": f"₹{round(product['price'] * 85)}",
            "category": category,
            "rating": product["rating"],
            "image": product["thumbnail"]

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