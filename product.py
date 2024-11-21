#!/usr/bin/env python
# coding: utf-8

# In[6]:


class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def update(self, name=None, price=None):
        if name:
            self.name = name
        if price:
            self.price = price

    def __str__(self):
        return f"Product ID: {self.product_id}, Name: {self.name}, Price: {self.price}"

class ProductManager:
    def __init__(self):
        self.products = {}

    # Product creation:
    def create_product(self, product_id, name, price):
        try:
            if product_id in self.products:
                print(f"Product {product_id} already exists.")
            else:
                self.products[product_id] = Product(product_id, name, price)
                print(f"Product {product_id} created.")
        except Exception as e:
            print(f"Error creating product {product_id}: {e}")

    # Product update:
    def update_product(self, product_id, name=None, price=None):
        try:
            if product_id in self.products:
                self.products[product_id].update(name, price)
            else:
                print(f"Product {product_id} does not exist.")
        except Exception as e:
            print(f"Error updating product {product_id}: {e}")

    # Product removal or deletion:
    def remove_product(self, product_id):
        try:
            if product_id in self.products:
                del self.products[product_id]
                print(f"Product {product_id} removed.")
            else:
                print(f"Product {product_id} does not exist.")
        except Exception as e:
            print(f"Error removing product {product_id}: {e}")

    # Print product details:
    def print_product(self, product_id):
        try:
            if product_id in self.products:
                print(self.products[product_id])
            else:
                print(f"Product {product_id} does not exist.")
        except Exception as e:
            print(f"Error printing product {product_id}: {e}")


# In[ ]:




