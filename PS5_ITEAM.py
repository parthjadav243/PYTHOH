
ps5_items = ["PS5 Console", "DualSense Controller", "Spider-Man: Miles Morales", "Charging Station"]

def display_items():
    print("Available PS5 Items:")
    for item in ps5_items:
        print("-", item)

def add_item(item):
    if item not in ps5_items:
        ps5_items.append(item)
        print(f"{item} added.")
    else:
        print(f"{item} already exists in the list.")

def remove_item(item):
    if item in ps5_items:
        ps5_items.remove(item)
        print(f"{item} removed.")
    else:
        print(f"{item} not found in the list.")

def search_item(item):
    if item in ps5_items:
        print(f"{item} is available.")
    else:
        print(f"{item} is not available.")

if __name__ == "__main__":
    display_items()
    add_item("Ratchet & Clank: Rift Apart")
    remove_item("Charging Station")
    search_item("PS5 Console")
