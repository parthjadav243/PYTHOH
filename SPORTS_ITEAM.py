

sports_items = ["Football", "Basketball", "Tennis Racket", "Cricket Bat"]

def display_items():
    print("Available Sports Items:")
    for item in sports_items:
        print("-", item)

def add_item(item):
    if item not in sports_items:
        sports_items.append(item)
        print(f"{item} added.")
    else:
        print(f"{item} already exists.")

def remove_item(item):
    if item in sports_items:
        sports_items.remove(item)
        print(f"{item} removed.")
    else:
        print(f"{item} not found.")

def search_item(item):
    if item in sports_items:
        print(f"{item} is available.")
    else:
        print(f"{item} is not in the list.")

if __name__ == "__main__":
    display_items()
    add_item("Volleyball")
    remove_item("Tennis Racket")
    search_item("Cricket Bat")
