# MyShop — Mini Amazon Clone

## Brief Description

MyShop is a basic Amazon-like e-commerce website built for learning Django.
Users can browse products, view product details, search for items, add products
to a cart, update quantities, remove items, and place an order through a simple
checkout form.

The cart is stored in the user session (no login required), and orders are
saved in a SQL database using Django models.

## Technologies / Tools Used

- **Python 3.14** — programming language
- **Django 6.1.2** — web framework (URLs, views, templates, ORM, admin)
- **SQLite (SQL)** — default Django SQL database, stored in `db.sqlite3`
- **HTML + CSS** — templates in `templates/`, styling in `static/style.css`
  (Gruvbox dark theme, square design)
- **Django Admin** — to add/edit products and view orders
- **venv + pip** — virtual environment and package management
- **Unsplash image URLs** — product images loaded via direct image links
  (`Product.image_url`), no file uploads needed

## Instructions to Run the Project

### 1. Go to the project folder

```bash
cd /home/samarth/Desktop/College/Mdm/TA1
```

### 2. Activate the virtual environment

```bash
source venv/bin/activate
```

> If starting from scratch on another machine:
> ```bash
> python3 -m venv venv
> source venv/bin/activate
> pip install -r requirements.txt
> ```

### 3. Install dependencies (already installed, for reference)

```bash
pip install -r requirements.txt
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Create an admin user (to add products)

```bash
python manage.py createsuperuser
```

### 6. Start the development server

```bash
python manage.py runserver
```

### 7. Open in browser

- Shop: http://127.0.0.1:8000/
- Product detail: http://127.0.0.1:8000/product/1/
- Cart: http://127.0.0.1:8000/cart/
- Checkout: http://127.0.0.1:8000/checkout/
- Admin: http://127.0.0.1:8000/admin/

8 sample products are already present in the database.

---

## Features

- Product list homepage with search (`?q=...`)
- Product detail page
- Add to Cart / Update Quantity / Remove from Cart
- Cart page with automatic total calculation
- Checkout form that creates an `Order` + `OrderItem` records and clears the cart
- Admin panel for products and orders
- Product images via pasted image URLs

## Project Structure

```
manage.py
requirements.txt
README.md
myshop/           # project config (settings.py has SQLite DB config)
  settings.py
  urls.py
shop/             # store app
  models.py       # Product, Order, OrderItem
  views.py        # product_list, product_detail, cart_*, checkout
  urls.py         # /, /product/<id>/, /cart/, /checkout/, ...
  forms.py        # CheckoutForm
  admin.py        # admin registration
  context_processors.py  # cart_count for navbar
templates/
  base.html
  shop/product_list.html
  shop/product_detail.html
  shop/cart.html
  shop/checkout.html
  shop/success.html
static/style.css  # Gruvbox + square theme
db.sqlite3        # SQLite SQL database
```

## How Product Images Work

Each product has an `image_url` field. Paste any direct image link there
(Admin → Products → Image URL), for example:

```
https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=400&q=80&auto=format&fit=crop
```

It renders with:

```html
<img src="{{ product.image_url }}" alt="{{ product.name }}">
```

## SQL Tables

- `shop_product` — id, name, description, price, stock, image_url
- `shop_order` — id, name, email, address, total, created_at
- `shop_orderitem` — id, order_id, product_id, quantity, price

Inspect with:

```bash
python manage.py dbshell
.tables
SELECT id, name, price FROM shop_product;
```
