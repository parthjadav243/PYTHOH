

makeup_items = ["Lipstick", "Foundation", "Mascara", "Eyeliner"]

def display_items():
    print("Available Makeup Accessories:")
    for item in makeup_items:
        print("-", item)

def add_item(item):
    if item not in makeup_items:
        makeup_items.append(item)
        print(f"{item} has been added.")
    else:
        print(f"{item} is already in the list.")

def remove_item(item):
    if item in makeup_items:
        makeup_items.remove(item)
        print(f"{item} has been removed.")
    else:
        print(f"{item} not found.")

def search_item(item):
    if item in makeup_items:
        print(f"{item} is available.")
    else:
        print(f"{item} is not available.")

if __name__ == "__main__":
    display_items()
    add_item("Blush")
    remove_item("Mascara")
    search_item("Eyeliner")
