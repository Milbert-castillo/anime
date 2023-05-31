class FoodItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Restaurant:
    def __init__(self, name, menu):
        self.name = name
        self.menu = menu


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.price
        return total


class FoodDeliveryApp:
    def __init__(self):
        self.restaurants = []

    def add_restaurant(self, restaurant):
        self.restaurants.append(restaurant)

    def remove_restaurant(self, restaurant):
        self.restaurants.remove(restaurant)

    def display_restaurants(self):
        for restaurant in self.restaurants:
            print(restaurant.name)

    def display_menu(self, restaurant):
        print(f"Menu for {restaurant.name}:")
        for item in restaurant.menu:
            print(f"{item.name} - ${item.price}")

    def place_order(self, restaurant):
        order = Order()
        print(f"Placing order from {restaurant.name}")
        print("Enter the item name to add to the order (or 'q' to quit):")
        self.display_menu(restaurant)

        while True:
            item_name = input()
            if item_name == 'q':
                break

            found = False
            for item in restaurant.menu:
                if item.name == item_name:
                    order.add_item(item)
                    found = True
                    break

            if found:
                print(f"{item_name} added to the order.")
            else:
                print(f"{item_name} is not available.")

        total = order.calculate_total()
        print(f"Order total: ${total}")
        print("Thank you for using our app!")

# Create food items
pizza = FoodItem("Pizza", 12.99)
burger = FoodItem("Burger", 8.99)
pasta = FoodItem("Pasta", 10.99)

# Create restaurants
restaurant1 = Restaurant("Pizza Place", [pizza, pasta])
restaurant2 = Restaurant("Burger Joint", [burger])

# Create food delivery app
app = FoodDeliveryApp()

# Add restaurants to the app
app.add_restaurant(restaurant1)
app.add_restaurant(restaurant2)

# Display available restaurants
app.display_restaurants()

# Place an order
selected_restaurant = restaurant1
app.place_order(selected_restaurant)