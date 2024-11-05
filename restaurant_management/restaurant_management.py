# restaurant_management.py

"""
    Restaurant Management System

    This module uses lists, sets, tuples, and dictionaries to manage restaurant data. It includes comprehensive business logic and demonstrates the use of common methods for each data structure.

    Data Structures:

    1. Lists: To store collections of menu items, orders, tables, and staff.
    2. Tuples: To store immutable menu item and staff details.
    3. Sets: To manage unique cuisines and roles.
    4. Dictionaries: To map menu item IDs and staff IDs to their details and manage table assignments.

    List of menu items with details (Item ID, Name, Cuisine, Price, Availability):
    menu_items = [
        (1, "Margherita Pizza", "Italian", 8.0, True),
        (2, "Tacos", "Mexican", 5.0, True),
        (3, "Sushi", "Japanese", 12.0, False),
        (4, "Pasta Carbonara", "Italian", 10.0, True),
        (5, "Burger", "American", 7.0, True)
    ]

    List of staff with details (Staff ID, Name, Age, Role):
    staff = [
        (101, "Alice", 30, "Chef"),
        (102, "Bob", 25, "Waiter"),
        (103, "Charlie", 28, "Manager"),
        (104, "Diana", 35, "Waiter"),
        (105, "Eve", 40, "Chef")
    ]

    List of tables (Table ID, Capacity, Availability):
    tables = [
        (1, 4, True),
        (2, 2, False),
        (3, 6, True),
        (4, 4, True),
        (5, 2, True)
    ]

    Set of unique cuisines:
    cuisines = set()

    Adding cuisines from menu items:
    for item in menu_items:
        cuisines.add(item[2])

    Set of unique roles:
    roles = set()

    Adding roles from staff:
    for member in staff:
        roles.add(member[3])

    Dictionary to map menu item IDs to their details:
    menu_catalog = {item[0]: item for item in menu_items}

    Dictionary to map staff IDs to their details:
    staff_catalog = {member[0]: member for member in staff}

    Dictionary to manage table assignments:
    table_assignments = {table[0]: table[2] for table in tables}

    Functions:

    List-Related Methods:
    1. find_menu_item_index(item_id): Finds the index of a menu item in the list.
    2. find_staff_index(staff_id): Finds the index of a staff member in the list.
    3. sort_menu_items_by_price(): Sorts menu items by price.
    4. sort_staff_by_age(): Sorts staff by age.
    5. reverse_tables(): Reverses the list of tables.
    6. append_menu_item(item): Appends a new menu item to the list.
    7. remove_menu_item(item_id): Removes a menu item from the list.

    Tuple-Related Methods:
    1. find_max_min_price(): Finds the maximum and minimum price of menu items.
    2. find_max_min_age_staff(): Finds the maximum and minimum age of staff.
    3. count_cuisine_occurrences(cuisine): Counts the occurrences of a specific cuisine.

    Set-Related Methods:
    1. add_cuisine(cuisine): Adds a new cuisine.
    2. remove_cuisine(cuisine): Removes a cuisine.
    3. list_all_cuisines(): Lists all cuisines.
    4. add_role(role): Adds a new role.
    5. remove_role(role): Removes a role.
    6. list_all_roles(): Lists all roles.
    7. find_common_cuisines(other_cuisines): Finds common cuisines between two sets.
    8. find_unique_cuisines(): Finds unique cuisines in the restaurant.
    9. clear_cuisines(): Clears all cuisines.

    Dictionary-Related Methods:
    1. add_menu_item(item_id, name, cuisine, price, availability): Adds a new menu item to the restaurant.
    2. remove_menu_item(item_id): Removes a menu item from the restaurant.
    3. get_menu_item_details(item_id): Gets menu item details.
    4. list_menu_items_by_cuisine(cuisine): Lists all menu items by cuisine.
    5. count_menu_items_by_cuisine(cuisine): Counts menu items by cuisine.
    6. add_staff(staff_id, name, age, role): Adds a new staff member to the restaurant.
    7. remove_staff(staff_id): Removes a staff member from the restaurant.
    8. get_staff_details(staff_id): Gets staff details.
    9. list_staff_by_role(role): Lists all staff by role.
    10. count_staff_by_role(role): Counts staff by role.
    11. update_menu_item_details(item_id, new_details): Updates menu item details.
    12. update_staff_details(staff_id, new_details): Updates staff details.
    13. merge_menu_catalogs(other_catalog): Merges two menu catalogs.
    14. merge_staff_catalogs(other_catalog): Merges two staff catalogs.
    15. get_all_menu_item_ids(): Gets all menu item IDs.
    16. get_all_staff_ids(): Gets all staff IDs.
    17. clear_menu_catalog(): Clears the menu catalog.
    18. clear_staff_catalog(): Clears the staff catalog.
"""
    
# restaurant_management.py

class RestaurantManagement:
    """
    Restaurant Management System

    This module uses lists, sets, tuples, and dictionaries to manage restaurant data. It includes comprehensive business logic and demonstrates the use of common methods for each data structure.

    Data Structures:

    1. Lists: To store collections of menu items, orders, tables, and staff.
    2. Tuples: To store immutable menu item and staff details.
    3. Sets: To manage unique cuisines and roles.
    4. Dictionaries: To map menu item IDs and staff IDs to their details and manage table assignments.
    """

    def __init__(self):
        # List of menu items with details (Item ID, Name, Cuisine, Price, Availability)
        self.menu_items = [
            (1, "Margherita Pizza", "Italian", 8.0, True),
            (2, "Tacos", "Mexican", 5.0, True),
            (3, "Sushi", "Japanese", 12.0, False),
            (4, "Pasta Carbonara", "Italian", 10.0, True),
            (5, "Burger", "American", 7.0, True)
        ]

        # List of staff with details (Staff ID, Name, Age, Role)
        self.staff = [
            (101, "Alice", 30, "Chef"),
            (102, "Bob", 25, "Waiter"),
            (103, "Charlie", 28, "Manager"),
            (104, "Diana", 35, "Waiter"),
            (105, "Eve", 40, "Chef")
        ]

        # List of tables (Table ID, Capacity, Availability)
        self.tables = [
            (1, 4, True),
            (2, 2, False),
            (3, 6, True),
            (4, 4, True),
            (5, 2, True)
        ]

        # Set of unique cuisines
        self.cuisines = set()

        # Adding cuisines from menu items
        for item in self.menu_items:
            self.cuisines.add(item[2])

        # Set of unique roles
        self.roles = set()

        # Adding roles from staff
        for member in self.staff:
            self.roles.add(member[3])

        # Dictionary to map menu item IDs to their details
        self.menu_catalog = {item[0]: item for item in self.menu_items}

        # Dictionary to map staff IDs to their details
        self.staff_catalog = {member[0]: member for member in self.staff}

        # Dictionary to manage table assignments
        self.table_assignments = {table[0]: table[2] for table in self.tables}

    # List-Related Methods
    def find_menu_item_index(self, item_id):
        """Finds the index of a menu item in the list."""
        for index, item in enumerate(self.menu_items):
            if item[0] == item_id:
                return index
        return -1

    def find_staff_index(self, staff_id):
        """Finds the index of a staff member in the list."""
        for index, member in enumerate(self.staff):
            if member[0] == staff_id:
                return index
        return -1

    def sort_menu_items_by_price(self):
        """Sorts menu items by price."""
        return sorted(self.menu_items, key=lambda item: item[3])

    def sort_staff_by_age(self):
        """Sorts staff by age."""
        return sorted(self.staff, key=lambda member: member[2])

    def reverse_tables(self):
        """Reverses the list of tables."""
        return self.tables[::-1]

    def append_menu_item(self, item):
        """Appends a new menu item to the list."""
        self.menu_items.append(item)
        self.menu_catalog[item[0]] = item
        self.cuisines.add(item[2])
        print(f"Menu item '{item[1]}' added.")

    def remove_menu_item(self, item_id):
        """Removes a menu item from the list."""
        index = self.find_menu_item_index(item_id)
        if index != -1:
            item = self.menu_items.pop(index)
            del self.menu_catalog[item_id]
            print(f"Menu item '{item[1]}' removed.")
        else:
            print(f"Menu item ID '{item_id}' not found.")

    # Tuple-Related Methods
    def find_max_min_price(self):
        """Finds the maximum and minimum price of menu items."""
        prices = [item[3] for item in self.menu_items]
        return max(prices), min(prices)

    def find_max_min_age_staff(self):
        """Finds the maximum and minimum age of staff."""
        ages = [member[2] for member in self.staff]
        return max(ages), min(ages)

    def count_cuisine_occurrences(self, cuisine):
        """Counts the occurrences of a specific cuisine."""
        return sum(1 for item in self.menu_items if item[2] == cuisine)

    # Set-Related Methods
    def add_cuisine(self, cuisine):
        """Adds a new cuisine."""
        self.cuisines.add(cuisine)
        print(f"Cuisine '{cuisine}' added.")

    def remove_cuisine(self, cuisine):
        """Removes a cuisine."""
        self.cuisines.discard(cuisine)
        print(f"Cuisine '{cuisine}' removed.")

    def list_all_cuisines(self):
        """Lists all cuisines."""
        return self.cuisines

    def add_role(self, role):
        """Adds a new role."""
        self.roles.add(role)
        print(f"Role '{role}' added.")

    def remove_role(self, role):
        """Removes a role."""
        self.roles.discard(role)
        print(f"Role '{role}' removed.")

    def list_all_roles(self):
        """Lists all roles."""
        return self.roles

    def find_common_cuisines(self, other_cuisines):
        """Finds common cuisines between two sets."""
        return self.cuisines.intersection(other_cuisines)

    def find_unique_cuisines(self):
        """Finds unique cuisines in the restaurant."""
        return self.cuisines.difference({"Italian", "Mexican", "Japanese", "American"})

    def clear_cuisines(self):
        """Clears all cuisines."""
        self.cuisines.clear()
        print("All cuisines cleared.")

    # Dictionary-Related Methods
    def add_menu_item(self, item_id, name, cuisine, price, availability):
        """Adds a new menu item to the restaurant."""
        if item_id not in self.menu_catalog:
            item = (item_id, name, cuisine, price, availability)
            self.append_menu_item(item)
        else:
            print(f"Menu item ID '{item_id}' already exists.")

    def remove_menu_item(self, item_id):
        """Removes a menu item from the restaurant."""
        if item_id in self.menu_catalog:
            item = self.menu_catalog.pop(item_id)
            self.menu_items.remove(item)
            print(f"Menu item '{item[1]}' removed.")
        else:
            print(f"Menu item ID '{item_id}' not found.")

    def get_menu_item_details(self, item_id):
        """Gets menu item details."""
        return self.menu_catalog.get(item_id, "Menu item not found.")

    def list_menu_items_by_cuisine(self, cuisine):
        """Lists all menu items by cuisine."""
        return [item for item in self.menu_items if item[2] == cuisine]

    def count_menu_items_by_cuisine(self, cuisine):
        """Counts menu items by cuisine."""
        return sum(1 for item in self.menu_items if item[2] == cuisine)

    def add_staff(self, staff_id, name, age, role):
        """Adds a new staff member to the restaurant."""
        if staff_id not in self.staff_catalog:
            member = (staff_id, name, age, role)
            self.staff.append(member)
            self.staff_catalog[staff_id] = member
            self.roles.add(role)
            print(f"Staff member '{name}' added.")
        else:
            print(f"Staff ID '{staff_id}' already exists.")

    def remove_staff(self, staff_id):
        """Removes a staff member from the restaurant."""
        if staff_id in self.staff_catalog:
            member = self.staff_catalog.pop(staff_id)
            self.staff.remove(member)
            print(f"Staff member '{member[1]}' removed.")
        else:
            print(f"Staff ID '{staff_id}' not found.")

    def get_staff_details(self, staff_id):
        """Gets staff details."""
        return self.staff_catalog.get(staff_id, "Staff member not found.")

    def list_staff_by_role(self, role):
        """Lists all staff by role."""
        return [member for member in self.staff if member[3] == role]

    def count_staff_by_role(self, role):
        """Counts staff by role."""
        return sum(1 for member in self.staff if member[3] == role)

    def update_menu_item_details(self, item_id, new_details):
        """Updates menu item details."""
        if item_id in self.menu_catalog:
            old_item = self.menu_catalog[item_id]
            self.menu_items.remove(old_item)
            self.menu_items.append(new_details)
            self.menu_catalog[item_id] = new_details
            print(f"Updated details for menu item ID '{item_id}'.")
        else:
            print(f"Menu item ID '{item_id}' not found.")

    def update_staff_details(self, staff_id, new_details):
        """Updates staff details."""
        if staff_id in self.staff_catalog:
            old_member = self.staff_catalog[staff_id]
            self.staff.remove(old_member)
            self.staff.append(new_details)
            self.staff_catalog[staff_id] = new_details
            print(f"Updated details for staff ID '{staff_id}'.")
        else:
            print(f"Staff ID '{staff_id}' not found.")

    def merge_menu_catalogs(self, other_catalog):
        """Merges two menu catalogs."""
        for item_id, details in other_catalog.items():
            if item_id not in self.menu_catalog:
                self.menu_catalog[item_id] = details
                self.menu_items.append(details)
                self.cuisines.add(details[2])
        print("Menu catalogs merged.")

    def merge_staff_catalogs(self, other_catalog):
        """Merges two staff catalogs."""
        for staff_id, details in other_catalog.items():
            if staff_id not in self.staff_catalog:
                self.staff_catalog[staff_id] = details
                self.staff.append(details)
                self.roles.add(details[3])
        print("Staff catalogs merged.")

    def get_all_menu_item_ids(self):
        """Gets all menu item IDs."""
        return list(self.menu_catalog.keys())

    def get_all_staff_ids(self):
        """Gets all staff IDs."""
        return list(self.staff_catalog.keys())

    def clear_menu_catalog(self):
        """Clears the menu catalog."""
        self.menu_catalog.clear()
        self.menu_items.clear()
        print("Menu catalog cleared.")

    def clear_staff_catalog(self):
        """Clears the staff catalog."""
        self.staff_catalog.clear()
        self.staff.clear()
        print("Staff catalog cleared.")

# Example usage
if __name__ == "__main__":
    restaurant = RestaurantManagement()

    print("Menu Catalog:")
    for item_id, details in restaurant.menu_catalog.items():
        print(f"{item_id}: {details}")

    print("\nStaff Available:")
    print(restaurant.staff)

    print("\nCuisines Available:")
    print(restaurant.cuisines)

    print("\nRoles Available:")
    print(restaurant.roles)

    print("\nTable Assignments:")
    for table_id, availability in restaurant.table_assignments.items():
        print(f"Table ID {table_id}: {'Available' if availability else 'Not Available'}")

    # Add and remove menu items
    restaurant.add_menu_item(6, "Salad", "Healthy", 6.0, True)
    restaurant.remove_menu_item(3)

    print("\nMenu Catalog After Changes:")
    for item_id, details in restaurant.menu_catalog.items():
        print(f"{item_id}: {details}")

    # Get menu item details
    print("\nMenu Item Details for ID 2:")
    print(restaurant.get_menu_item_details(2))

    # List menu items by cuisine
    print("\nMenu Items in Italian Cuisine:")
    print(restaurant.list_menu_items_by_cuisine("Italian"))

    # Count menu items by cuisine
    print("\nCount of Menu Items in American Cuisine:")
    print(restaurant.count_menu_items_by_cuisine("American"))

    # Find menu item index
    print("\nIndex of Menu Item ID 2:")
    print(restaurant.find_menu_item_index(2))

    # Add and remove cuisines
    restaurant.add_cuisine("French")
    restaurant.remove_cuisine("Japanese")

    # List all cuisines
    print("\nAll Cuisines:")
    print(restaurant.list_all_cuisines())

    # Add and remove roles
    restaurant.add_role("Bartender")
    restaurant.remove_role("Manager")

    # List all roles
    print("\nAll Roles:")
    print(restaurant.list_all_roles())

    # Sort menu items by price
    print("\nMenu Items Sorted by Price:")
    for item in restaurant.sort_menu_items_by_price():
        print(item)

    # Reverse the list of tables
    print("\nReversed List of Tables:")
    print(restaurant.reverse_tables())

    # Find the maximum and minimum price of menu items
    max_price, min_price = restaurant.find_max_min_price()
    print(f"\nMaximum Price: {max_price}, Minimum Price: {min_price}")

    # Find the maximum and minimum age of staff
    max_age, min_age = restaurant.find_max_min_age_staff()
    print(f"\nMaximum Age of Staff: {max_age}, Minimum Age of Staff: {min_age}")

    # Count the occurrences of a specific cuisine
    print(f"\nOccurrences of 'Italian': {restaurant.count_cuisine_occurrences('Italian')}")

    # Find common cuisines between two sets
    other_cuisines = {"Italian", "French", "Chinese"}
    print(f"\nCommon Cuisines: {restaurant.find_common_cuisines(other_cuisines)}")

    # Find unique cuisines in the restaurant
    print(f"\nUnique Cuisines: {restaurant.find_unique_cuisines()}")

    # Update menu item details
    restaurant.update_menu_item_details(2, (2, "Tacos", "Mexican", 4.5, True))
    print(f"\nUpdated Menu Item Details for ID 2: {restaurant.get_menu_item_details(2)}")

    # Merge two menu catalogs
    other_menu_catalog = {
        7: (7, "Steak", "American", 15.0, True),
        8: (8, "Ramen", "Japanese", 9.0, True)
    }
    restaurant.merge_menu_catalogs(other_menu_catalog)
    print("\nMerged Menu Catalog:")
    for item_id, details in restaurant.menu_catalog.items():
        print(f"{item_id}: {details}")

    # Merge two staff catalogs
    other_staff_catalog = {
        106: (106, "Frank", 32, "Bartender"),
        107: (107, "Grace", 29, "Waiter")
    }
    restaurant.merge_staff_catalogs(other_staff_catalog)
    print("\nMerged Staff Catalog:")
    for staff_id, details in restaurant.staff_catalog.items():
        print(f"{staff_id}: {details}")

    # Get all menu item IDs
    print("\nAll Menu Item IDs:")
    print(restaurant.get_all_menu_item_ids())

    # Get all staff IDs
    print("\nAll Staff IDs:")
    print(restaurant.get_all_staff_ids())

    # Clear the menu catalog
    restaurant.clear_menu_catalog()
    print("\nMenu Catalog After Clearing:")
    print(restaurant.menu_catalog)

    # Clear the staff catalog
    restaurant.clear_staff_catalog()
    print("\nStaff Catalog After Clearing:")
    print(restaurant.staff_catalog)