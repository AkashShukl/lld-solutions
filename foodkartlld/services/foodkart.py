import threading
from exceptions import RestaurantNotFoundError

from models.restraunt import FoodItem, Restaurant
from models.users import User


class Foodkart:
    _instance = None
    _lock = threading.Lock()

    @staticmethod
    def get_instance():
        if Foodkart._instance is None:
            with Foodkart._lock:
                if Foodkart._instance is None:
                    Foodkart._instance = Foodkart()
        return Foodkart._instance


    def __init__(self):
        self.users = {}
        self.restaurants = {}

    def get_restraunt(self,name):
        try:
            return self.restaurants[name]
        except KeyError:
            raise RestaurantNotFoundError(f"Restaurant '{name}' does not exist")

    def register_user(self, name, gender, phoneNumber, pincode):
        user = User(name, gender, phoneNumber, pincode)
        self.users[phoneNumber] = user

    def login_user(self, phoneNumber):
        try:
            self.current_user = self.users.get(phoneNumber)
        except KeyError:
            raise KeyError(f"User -> '{phoneNumber}', does not exist")

    def register_restaurant(self, name, serviceable_pincodes, food_name, food_price, initial_quantity):
        food_item = FoodItem(food_name, food_price, initial_quantity)
        restaurant = Restaurant(
            name, serviceable_pincodes.split('/'), food_item)
        self.restaurants[name] = restaurant

    def place_order(self, restaurant_name, quantity):
        restaurant = self.get_restraunt(restaurant_name)
        if self.current_user.pincode in restaurant.serviceable_pincodes and restaurant.food_item.quantity >= quantity:
            restaurant.food_item.quantity -= quantity
            print("Order Placed Successfully.")
        else:
            print("Cannot place order")

    def create_review(self, restaurant_name, rating, comment=""):
        restaurant = self.get_restraunt(restaurant_name)
        restaurant.add_review(rating, comment)

    def show_restaurants(self, sort_by="rating"):
        sorted_restaurants = None
        if sort_by == "rating":
            sorted_restaurants = sorted(self.restaurants.values(
            ), key=lambda r: getattr(r, sort_by), reverse=True)
        else:
            sorted_restaurants = sorted(self.restaurants.values(
            ), key=lambda restraunt: restraunt.food_item.price, reverse=True)
        for restaurant in sorted_restaurants:
            print(f"{restaurant.name}, {restaurant.food_item.name}")

    def update_quantity(self, restaurant_name, quantity_to_add):
        restaurant = self.get_restraunt(restaurant_name)
        restaurant.increase_quantity(quantity_to_add)
        print(f"{restaurant.name}, {restaurant.food_item.quantity}")

    def update_location(self, restaurant_name, new_serviceable_pincodes):
        restaurant = self.get_restraunt(restaurant_name)
        restaurant.serviceable_pincodes = new_serviceable_pincodes.split('/')

