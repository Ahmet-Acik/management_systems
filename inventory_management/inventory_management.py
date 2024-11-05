# inventory_management.py

"""
    Inventory Management System

    This module uses lists, sets, tuples, and dictionaries to manage inventory data. It includes comprehensive business logic and demonstrates the use of common methods for each data structure.

    Data Structures:

    1. Lists: To store collections of products, categories, and suppliers.
    2. Tuples: To store immutable product and supplier details.
    3. Sets: To manage unique categories and product names.
    4. Dictionaries: To map product IDs and supplier IDs to their details and manage stock levels.

    List of products with details (Product ID, Name, Category, Supplier ID, Price, Stock):
    products = [
        (1, "Laptop", "Electronics", 101, 1000.0, 50),
        (2, "Smartphone", "Electronics", 102, 500.0, 200),
        (3, "Desk Chair", "Furniture", 103, 150.0, 100),
        (4, "Notebook", "Stationery", 104, 2.0, 500),
        (5, "Pen", "Stationery", 104, 1.0, 1000)
    ]

    List of suppliers with details (Supplier ID, Name, Contact):
    suppliers = [
        (101, "Tech Supplies Inc.", "123-456-7890"),
        (102, "Mobile World", "234-567-8901"),
        (103, "Office Furniture Co.", "345-678-9012"),
        (104, "Stationery Hub", "456-789-0123")
    ]

    Set of unique categories:
    categories = set()

    Adding categories from products:
    for product in products:
        categories.add(product[2])

    Set of unique product names:
    product_names = set()

    Adding product names from products:
    for product in products:
        product_names.add(product[1])

    Dictionary to map product IDs to their details:
    product_catalog = {product[0]: product for product in products}

    Dictionary to map supplier IDs to their details:
    supplier_catalog = {supplier[0]: supplier for supplier in suppliers}

    Dictionary to manage stock levels:
    stock_levels = {product[0]: product[5] for product in products}

    Functions:

    List-Related Methods:
    1. find_product_index(product_id): Finds the index of a product in the list.
    2. sort_products_by_price(): Sorts products by price.
    3. reverse_suppliers(): Reverses the list of suppliers.
    4. append_product(product): Appends a new product to the list.
    5. remove_product(product_id): Removes a product from the list.

    Tuple-Related Methods:
    1. find_max_min_price(): Finds the maximum and minimum price of products.
    2. count_category_occurrences(category): Counts the occurrences of a specific category.

    Set-Related Methods:
    1. add_category(category): Adds a new category.
    2. remove_category(category): Removes a category.
    3. list_all_categories(): Lists all categories.
    4. add_product_name(product_name): Adds a new product name.
    5. remove_product_name(product_name): Removes a product name.
    6. list_all_product_names(): Lists all product names.
    7. find_common_categories(other_categories): Finds common categories between two sets.
    8. find_unique_categories(): Finds unique categories in the inventory.
    9. clear_categories(): Clears all categories.

    Dictionary-Related Methods:
    1. add_product(product_id, name, category, supplier_id, price, stock): Adds a new product to the inventory.
    2. remove_product(product_id): Removes a product from the inventory.
    3. get_product_details(product_id): Gets product details.
    4. list_products_by_category(category): Lists all products by category.
    5. count_products_by_category(category): Counts products by category.
    6. add_supplier(supplier_id, name, contact): Adds a new supplier to the inventory.
    7. remove_supplier(supplier_id): Removes a supplier from the inventory.
    8. get_supplier_details(supplier_id): Gets supplier details.
    9. update_product_details(product_id, new_details): Updates product details.
    10. update_supplier_details(supplier_id, new_details): Updates supplier details.
    11. merge_product_catalogs(other_catalog): Merges two product catalogs.
    12. merge_supplier_catalogs(other_catalog): Merges two supplier catalogs.
    13. get_all_product_ids(): Gets all product IDs.
    14. get_all_supplier_ids(): Gets all supplier IDs.
    15. clear_product_catalog(): Clears the product catalog.
    16. clear_supplier_catalog(): Clears the supplier catalog.
"""
# inventory_management.py

class InventoryManagement:
    """
    Inventory Management System

    This module uses lists, sets, tuples, and dictionaries to manage inventory data. It includes comprehensive business logic and demonstrates the use of common methods for each data structure.

    Data Structures:

    1. Lists: To store collections of products, categories, and suppliers.
    2. Tuples: To store immutable product and supplier details.
    3. Sets: To manage unique categories and product names.
    4. Dictionaries: To map product IDs and supplier IDs to their details and manage stock levels.
    """

    def __init__(self):
        # List of products with details (Product ID, Name, Category, Supplier ID, Price, Stock)
        self.products = [
            (1, "Laptop", "Electronics", 101, 1000.0, 50),
            (2, "Smartphone", "Electronics", 102, 500.0, 200),
            (3, "Desk Chair", "Furniture", 103, 150.0, 100),
            (4, "Notebook", "Stationery", 104, 2.0, 500),
            (5, "Pen", "Stationery", 104, 1.0, 1000)
        ]

        # List of suppliers with details (Supplier ID, Name, Contact)
        self.suppliers = [
            (101, "Tech Supplies Inc.", "123-456-7890"),
            (102, "Mobile World", "234-567-8901"),
            (103, "Office Furniture Co.", "345-678-9012"),
            (104, "Stationery Hub", "456-789-0123")
        ]

        # Set of unique categories
        self.categories = set()

        # Adding categories from products
        for product in self.products:
            self.categories.add(product[2])

        # Set of unique product names
        self.product_names = set()

        # Adding product names from products
        for product in self.products:
            self.product_names.add(product[1])

        # Dictionary to map product IDs to their details
        self.product_catalog = {product[0]: product for product in self.products}

        # Dictionary to map supplier IDs to their details
        self.supplier_catalog = {supplier[0]: supplier for supplier in self.suppliers}

        # Dictionary to manage stock levels
        self.stock_levels = {product[0]: product[5] for product in self.products}

    # List-Related Methods
    def find_product_index(self, product_id):
        """Finds the index of a product in the list."""
        for index, product in enumerate(self.products):
            if product[0] == product_id:
                return index
        return -1

    def sort_products_by_price(self):
        """Sorts products by price."""
        return sorted(self.products, key=lambda product: product[4])

    def reverse_suppliers(self):
        """Reverses the list of suppliers."""
        return self.suppliers[::-1]

    def append_product(self, product):
        """Appends a new product to the list."""
        self.products.append(product)
        self.product_catalog[product[0]] = product
        self.categories.add(product[2])
        self.product_names.add(product[1])
        self.stock_levels[product[0]] = product[5]
        print(f"Product '{product[1]}' added.")

    def remove_product(self, product_id):
        """Removes a product from the list."""
        index = self.find_product_index(product_id)
        if index != -1:
            product = self.products.pop(index)
            del self.product_catalog[product_id]
            del self.stock_levels[product_id]
            print(f"Product '{product[1]}' removed.")
        else:
            print(f"Product ID '{product_id}' not found.")

    # Tuple-Related Methods
    def find_max_min_price(self):
        """Finds the maximum and minimum price of products."""
        prices = [product[4] for product in self.products]
        return max(prices), min(prices)

    def count_category_occurrences(self, category):
        """Counts the occurrences of a specific category."""
        return sum(1 for product in self.products if product[2] == category)

    # Set-Related Methods
    def add_category(self, category):
        """Adds a new category."""
        self.categories.add(category)
        print(f"Category '{category}' added.")

    def remove_category(self, category):
        """Removes a category."""
        self.categories.discard(category)
        print(f"Category '{category}' removed.")

    def list_all_categories(self):
        """Lists all categories."""
        return self.categories

    def add_product_name(self, product_name):
        """Adds a new product name."""
        self.product_names.add(product_name)
        print(f"Product name '{product_name}' added.")

    def remove_product_name(self, product_name):
        """Removes a product name."""
        self.product_names.discard(product_name)
        print(f"Product name '{product_name}' removed.")

    def list_all_product_names(self):
        """Lists all product names."""
        return self.product_names

    def find_common_categories(self, other_categories):
        """Finds common categories between two sets."""
        return self.categories.intersection(other_categories)

    def find_unique_categories(self):
        """Finds unique categories in the inventory."""
        return self.categories.difference({"Electronics", "Furniture", "Stationery"})

    def clear_categories(self):
        """Clears all categories."""
        self.categories.clear()
        print("All categories cleared.")

    # Dictionary-Related Methods
    def add_product(self, product_id, name, category, supplier_id, price, stock):
        """Adds a new product to the inventory."""
        if product_id not in self.product_catalog:
            product = (product_id, name, category, supplier_id, price, stock)
            self.append_product(product)
        else:
            print(f"Product ID '{product_id}' already exists.")

    def remove_product(self, product_id):
        """Removes a product from the inventory."""
        if product_id in self.product_catalog:
            product = self.product_catalog.pop(product_id)
            self.products.remove(product)
            self.stock_levels.pop(product_id)
            print(f"Product '{product[1]}' removed.")
        else:
            print(f"Product ID '{product_id}' not found.")

    def get_product_details(self, product_id):
        """Gets product details."""
        return self.product_catalog.get(product_id, "Product not found.")

    def list_products_by_category(self, category):
        """Lists all products by category."""
        return [product for product in self.products if product[2] == category]

    def count_products_by_category(self, category):
        """Counts products by category."""
        return sum(1 for product in self.products if product[2] == category)

    def add_supplier(self, supplier_id, name, contact):
        """Adds a new supplier to the inventory."""
        if supplier_id not in self.supplier_catalog:
            supplier = (supplier_id, name, contact)
            self.suppliers.append(supplier)
            self.supplier_catalog[supplier_id] = supplier
            print(f"Supplier '{name}' added.")
        else:
            print(f"Supplier ID '{supplier_id}' already exists.")

    def remove_supplier(self, supplier_id):
        """Removes a supplier from the inventory."""
        if supplier_id in self.supplier_catalog:
            supplier = self.supplier_catalog.pop(supplier_id)
            self.suppliers.remove(supplier)
            print(f"Supplier '{supplier[1]}' removed.")
        else:
            print(f"Supplier ID '{supplier_id}' not found.")

    def get_supplier_details(self, supplier_id):
        """Gets supplier details."""
        return self.supplier_catalog.get(supplier_id, "Supplier not found.")

    def update_product_details(self, product_id, new_details):
        """Updates product details."""
        if product_id in self.product_catalog:
            old_product = self.product_catalog[product_id]
            self.products.remove(old_product)
            self.products.append(new_details)
            self.product_catalog[product_id] = new_details
            self.stock_levels[product_id] = new_details[5]
            print(f"Updated details for product ID '{product_id}'.")
        else:
            print(f"Product ID '{product_id}' not found.")

    def update_supplier_details(self, supplier_id, new_details):
        """Updates supplier details."""
        if supplier_id in self.supplier_catalog:
            old_supplier = self.supplier_catalog[supplier_id]
            self.suppliers.remove(old_supplier)
            self.suppliers.append(new_details)
            self.supplier_catalog[supplier_id] = new_details
            print(f"Updated details for supplier ID '{supplier_id}'.")
        else:
            print(f"Supplier ID '{supplier_id}' not found.")

    def merge_product_catalogs(self, other_catalog):
        """Merges two product catalogs."""
        for product_id, details in other_catalog.items():
            if product_id not in self.product_catalog:
                self.product_catalog[product_id] = details
                self.products.append(details)
                self.stock_levels[product_id] = details[5]
                self.categories.add(details[2])
                self.product_names.add(details[1])
        print("Product catalogs merged.")

    def merge_supplier_catalogs(self, other_catalog):
        """Merges two supplier catalogs."""
        for supplier_id, details in other_catalog.items():
            if supplier_id not in self.supplier_catalog:
                self.supplier_catalog[supplier_id] = details
                self.suppliers.append(details)
        print("Supplier catalogs merged.")

    def get_all_product_ids(self):
        """Gets all product IDs."""
        return list(self.product_catalog.keys())

    def get_all_supplier_ids(self):
        """Gets all supplier IDs."""
        return list(self.supplier_catalog.keys())

    def clear_product_catalog(self):
        """Clears the product catalog."""
        self.product_catalog.clear()
        self.products.clear()
        self.stock_levels.clear()
        print("Product catalog cleared.")

    def clear_supplier_catalog(self):
        """Clears the supplier catalog."""
        self.supplier_catalog.clear()
        self.suppliers.clear()
        print("Supplier catalog cleared.")

# Example usage
if __name__ == "__main__":
    inventory = InventoryManagement()

    print("Product Catalog:")
    for product_id, details in inventory.product_catalog.items():
        print(f"{product_id}: {details}")

    print("\nSuppliers Available:")
    print(inventory.suppliers)

    print("\nCategories Available:")
    print(inventory.categories)

    print("\nProduct Names Available:")
    print(inventory.product_names)

    print("\nStock Levels:")
    for product_id, stock in inventory.stock_levels.items():
        print(f"{product_id}: {stock}")

    # Add and remove products
    inventory.add_product(6, "Tablet", "Electronics", 102, 300.0, 150)
    inventory.remove_product(3)

    print("\nProduct Catalog After Changes:")
    for product_id, details in inventory.product_catalog.items():
        print(f"{product_id}: {details}")

    # Get product details
    print("\nProduct Details for ID 2:")
    print(inventory.get_product_details(2))

    # List products by category
    print("\nProducts in Electronics Category:")
    print(inventory.list_products_by_category("Electronics"))

    # Count products by category
    print("\nCount of Products in Stationery Category:")
    print(inventory.count_products_by_category("Stationery"))

    # Find product index
    print("\nIndex of Product ID 2:")
    print(inventory.find_product_index(2))

    # Add and remove categories
    inventory.add_category("Books")
    inventory.remove_category("Furniture")

    # List all categories
    print("\nAll Categories:")
    print(inventory.list_all_categories())

    # Add and remove product names
    inventory.add_product_name("Eraser")
    inventory.remove_product_name("Notebook")

    # List all product names
    print("\nAll Product Names:")
    print(inventory.list_all_product_names())

    # Sort products by price
    print("\nProducts Sorted by Price:")
    for product in inventory.sort_products_by_price():
        print(product)

    # Reverse the list of suppliers
    print("\nReversed List of Suppliers:")
    print(inventory.reverse_suppliers())

    # Find the maximum and minimum price of products
    max_price, min_price = inventory.find_max_min_price()
    print(f"\nMaximum Price: {max_price}, Minimum Price: {min_price}")

    # Count the occurrences of a specific category
    print(f"\nOccurrences of 'Electronics': {inventory.count_category_occurrences('Electronics')}")

    # Find common categories between two sets
    other_categories = {"Electronics", "Books", "Toys"}
    print(f"\nCommon Categories: {inventory.find_common_categories(other_categories)}")

    # Find unique categories in the inventory
    print(f"\nUnique Categories: {inventory.find_unique_categories()}")

    # Update product details
    inventory.update_product_details(2, (2, "Smartphone", "Electronics", 102, 450.0, 180))
    print(f"\nUpdated Product Details for ID 2: {inventory.get_product_details(2)}")

    # Merge two product catalogs
    other_product_catalog = {
        7: (7, "Monitor", "Electronics", 101, 200.0, 80),
        8: (8, "Keyboard", "Electronics", 101, 50.0, 300)
    }
    inventory.merge_product_catalogs(other_product_catalog)
    print("\nMerged Product Catalog:")
    for product_id, details in inventory.product_catalog.items():
        print(f"{product_id}: {details}")

    # Merge two supplier catalogs
    other_supplier_catalog = {
        105: (105, "Gadget World", "567-890-1234"),
        106: (106, "Office Supplies Co.", "678-901-2345")
    }
    inventory.merge_supplier_catalogs(other_supplier_catalog)
    print("\nMerged Supplier Catalog:")
    for supplier_id, details in inventory.supplier_catalog.items():
        print(f"{supplier_id}: {details}")

    # Get all product IDs
    print("\nAll Product IDs:")
    print(inventory.get_all_product_ids())

    # Get all supplier IDs
    print("\nAll Supplier IDs:")
    print(inventory.get_all_supplier_ids())

    # Clear the product catalog
    inventory.clear_product_catalog()
    print("\nProduct Catalog After Clearing:")
    print(inventory.product_catalog)

    # Clear the supplier catalog
    inventory.clear_supplier_catalog()
    print("\nSupplier Catalog After Clearing:")
    print(inventory.supplier_catalog)