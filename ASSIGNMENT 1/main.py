class Product:
    id: int
    name: str
    price: float
    category: str
    in_stock: int   

    def __init__(self, id: int, name: str, price: float, category: str, in_stock: int):
        self.id = id
        self.name = name
        self.price = price
        self.category = category
        self.in_stock = in_stock
from fastapi import FastAPI
from main import Product
app = FastAPI()
@app.get("/")

def greet():
    return "welcome to the world of programming!"
products = [
    {"id": 1, "name": "Laptop", "price": 75000, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "Mouse", "price": 500, "category": "Electronics", "in_stock": True},
    {"id": 3, "name": "Keyboard", "price": 1500, "category": "Electronics", "in_stock": True},
    {"id": 4, "name": "Book", "price": 12000, "category": "Stationery", "in_stock": True},

    # ➕ Newly added products
    {"id": 5, "name": "Laptop Stand", "price": 1200, "category": "Stationery", "in_stock": True},
    {"id": 6, "name": "Mechanical Keyboard", "price": 4500, "category": "Accessories", "in_stock": True},
    {"id": 7, "name": "Webcam", "price": 2500, "category": "Electronics", "in_stock": True}
]


           
            

@app.get('/products')
def get_products():
    return {
        "products": products,
        "total": len(products)
    }
@app.get("/products/instock")
def get_instock_products():
    instock_products = [
        product for product in products
        if product["in_stock"] == True
    ]

    return {
        "in_stock_products": instock_products,
        "count": len(instock_products)
    }


@app.get("/products/category/{category_name}")
def get_products_by_category(category_name: str):
    filtered_products = [
        product for product in products
        if product["category"].lower() == category_name.lower()
    ]

    if not filtered_products:
        return {"error": "No products found in this category"}

    return {
        "products": filtered_products,
        "total": len(filtered_products)
    }
@app.get("/products/search/{keyword}")
def search_products(keyword: str):
    matched_products = [
        product for product in products
        if keyword.lower() in product["name"].lower()
    ]

    if not matched_products:
        return {"message": "No products matched your search"}

    return {
        "products": matched_products,
        "total": len(matched_products)
    }
@app.get("/products/deals")
def get_product_deals():
    if not products:
        return {"message": "No products available"}

    best_deal = min(products, key=lambda p: p["price"])
    premium_pick = max(products, key=lambda p: p["price"])

    return {
        "best_deal": best_deal,
        "premium_pick": premium_pick
    }
@app.get('/products/{product_id}')
def get_product(product_id: int):
    item=0
    for product in products:
       if product.id == product_id:
            return product 
       
    return 'Product not found'
@app.get("/store/summary")
def store_summary():
    total_products = len(products)
    in_stock = len([p for p in products if p["in_stock"]])
    out_of_stock = total_products - in_stock

    categories = list(set([p["category"] for p in products]))

    return {
        "store_name": "My E-commerce Store",
        "total_products": total_products,
        "in_stock": in_stock,
        "out_of_stock": out_of_stock,
        "categories": categories
    }
