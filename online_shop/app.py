from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "magazia123"

products = [
    {"id": 1, "name": "ლეპტოპი", "price": 2500},
    {"id": 2, "name": "ტელეფონი", "price": 1200},
    {"id": 3, "name": "ყურსასმენი", "price": 150},
    {"id": 4, "name": "კლავიატურა", "price": 90},
    {"id": 5, "name": "მაუსი", "price": 45},
    {"id": 6, "name": "მონიტორი", "price": 600},
]

orders = []


def get_cart():
    return session.get("cart", {})


def cart_items():
    cart = get_cart()
    items = []
    total = 0
    for product in products:
        qty = cart.get(str(product["id"]), 0)
        if qty > 0:
            price = product["price"] * qty
            items.append({"product": product, "qty": qty, "price": price})
            total += price
    return items, total


@app.route("/")
def index():
    search = request.args.get("q", "").strip()
    shown = [p for p in products if search.lower() in p["name"].lower()]
    cart = get_cart()
    count = sum(cart.values())
    return render_template("index.html", products=shown, count=count, search=search)


@app.route("/add/<int:product_id>")
def add(product_id):
    cart = get_cart()
    key = str(product_id)
    cart[key] = cart.get(key, 0) + 1
    session["cart"] = cart
    return redirect(url_for("index"))


@app.route("/remove/<int:product_id>")
def remove(product_id):
    cart = get_cart()
    key = str(product_id)
    if key in cart:
        cart[key] -= 1
        if cart[key] <= 0:
            del cart[key]
    session["cart"] = cart
    return redirect(url_for("cart"))


@app.route("/cart")
def cart():
    items, total = cart_items()
    return render_template("cart.html", items=items, total=total)


@app.route("/checkout", methods=["POST"])
def checkout():
    items, total = cart_items()
    if not items:
        return redirect(url_for("index"))
    name = request.form.get("name", "").strip()
    address = request.form.get("address", "").strip()
    if not name or not address:
        return redirect(url_for("cart"))
    orders.append({"name": name, "address": address, "products": items, "total": total})
    session["cart"] = {}
    return render_template("success.html", name=name, total=total)


@app.route("/orders")
def order_list():
    return render_template("orders.html", orders=orders)


if __name__ == "__main__":
    app.run(debug=True)
