from django.core.management.base import BaseCommand

from shop.models import Product

PRODUCTS = [
    {
        "name": "Laptop",
        "description": "14 inch display, 16GB RAM, 512GB SSD laptop for college work.",
        "price": 49999,
        "stock": 10,
        "image_url": "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=400&q=80&auto=format&fit=crop",
    },
    {
        "name": "Headphones",
        "description": "Wireless noise-cancelling headphones with long battery.",
        "price": 2999,
        "stock": 25,
        "image_url": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400&q=80&auto=format&fit=crop",
    },
    {
        "name": "Shoes",
        "description": "Comfortable running shoes for daily use.",
        "price": 1999,
        "stock": 30,
        "image_url": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400&q=80&auto=format&fit=crop",
    },
    {
        "name": "Backpack",
        "description": "Water-resistant college backpack with laptop sleeve.",
        "price": 1299,
        "stock": 20,
        "image_url": "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=400&q=80&auto=format&fit=crop",
    },
    {
        "name": "Smart Watch",
        "description": "Fitness tracking smart watch with heart-rate monitor.",
        "price": 3499,
        "stock": 15,
        "image_url": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400&q=80&auto=format&fit=crop",
    },
    {
        "name": "Water Bottle",
        "description": "1L steel insulated water bottle.",
        "price": 599,
        "stock": 50,
        "image_url": "https://images.unsplash.com/photo-1602143407151-7111542de6e8?w=400&q=80&auto=format&fit=crop",
    },
    {
        "name": "Novel Book",
        "description": "Bestseller fiction novel, 300 pages.",
        "price": 399,
        "stock": 40,
        "image_url": "https://images.unsplash.com/photo-1544947950-fa07a98d237f?w=400&q=80&auto=format&fit=crop",
    },
    {
        "name": "Keyboard",
        "description": "Mechanical RGB keyboard for coding.",
        "price": 2499,
        "stock": 12,
        "image_url": "https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=400&q=80&auto=format&fit=crop",
    },
]


class Command(BaseCommand):
    help = "Load 8 sample products with Unsplash images (idempotent)."

    def handle(self, *args, **options):
        created = 0
        for item in PRODUCTS:
            _, was_created = Product.objects.get_or_create(
                name=item["name"], defaults=item
            )
            created += int(was_created)
        self.stdout.write(
            self.style.SUCCESS(f"Done. {created} new products added ({Product.objects.count()} total).")
        )
