import csv


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - ${self.price} - Qty: {self.quantity}"

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise Exception("Quantity cannot be negative.")
        self._quantity = value


class Electronic(Product):
    def __init__(self, name, price, quantity, warranty_months):
        super().__init__(name, price, quantity)
        self.warranty_months = warranty_months

    def __str__(self):
        return f"{super().__str__()} - Warranty: {self.warranty_months} months"


class Clothing(Product):
    def __init__(self, name, price, quantity, size):
        super().__init__(name, price, quantity)
        self.size = size

    def __str__(self):
        return f"{super().__str__()} - Size: {self.size}"


class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if product.name in self.products:
            print(f"Product '{product.name}' already exists in inventory.")
            return
        self.products[product.name] = product
        print(f"Product '{product.name}' added successfully.")

    def update_product(self, name, price=None, quantity=None):
        if name not in self.products:
            print(f"Product '{name}' not found in inventory.")
            return
        if price is not None:
            self.products[name].price = price
        if quantity is not None:
            self.products[name].quantity = quantity
        print(f"Product '{name}' updated successfully.")

    def remove_product(self, name):
        if name not in self.products:
            print(f"Product '{name}' not found in inventory.")
            return
        del self.products[name]
        print(f"Product '{name}' removed successfully.")

    def display_inventory(self):
        if not self.products:
            print("Inventory is empty.")
            return
        for product in self.products.values():
            print(product)


class Store:
    def __init__(self, name):
        self.name = name
        self.inventory = Inventory()

    def add_product_to_store(self, product):
        self.inventory.add_product(product)

    def update_product_in_store(self, name, price=None, quantity=None):
        self.inventory.update_product(name, price, quantity)

    def remove_product_from_store(self, name):
        self.inventory.remove_product(name)

    def show_store_inventory(self):
        print(f"Inventory for store '{self.name}':")
        self.inventory.display_inventory()
    
    def load_products_from_csv(self, filename):
        try:
            with open(filename, newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    product_type = row["type"].lower()
                    name = row["name"]
                    price = float(row["price"])
                    quantity = int(row["quantity"])

                    if product_type == "electronic":
                        warranty_months = int(row.get("warranty_months", 0))
                        product = Electronic(name, price, quantity, warranty_months)
                    elif product_type == "clothing":
                        size = row.get("size", "M")
                        product = Clothing(name, price, quantity, size)
                    else:
                        product = Product(name, price, quantity)

                    self.add_product_to_store(product)
        except FileNotFoundError:
            print(f"File {filename} not found.")
        except Exception as e:
            print(f"Error loading CSV: {e}")


# Example usage
if __name__ == "__main__":
    store = Store("Tech & Fashion Store")

    # Adding products
    laptop = Electronic("Laptop", 1200, 10, 24)
    shirt = Clothing("Shirt", 25, 50, "M")

    # shirt.quantity = -45  # Update quantity using setter

    store.add_product_to_store(laptop)
    store.add_product_to_store(shirt)

    # Display inventory
    store.show_store_inventory()

    # Update a product
    store.update_product_in_store(laptop.name, price=1100, quantity=8)

    # Remove a product
    store.remove_product_from_store(shirt.name)

    store.load_products_from_csv("products.csv")

    # Display updated inventory
    store.show_store_inventory()