from services.foodkart import Foodkart


if __name__ == "__main__":
    foodkart = Foodkart()

    foodkart.register_user("Pralove", "M", "phoneNumber-1", "HSR")
    foodkart.register_user("Nitesh", "M", "phoneNumber-2", "BTM")
    foodkart.register_user("Vatsal", "M", "phoneNumber-3", "BTM")

    foodkart.login_user("phoneNumber-1")

    foodkart.register_restaurant("Food Court-1", "BTM/HSR", "NI Thali", 100, 5)
    foodkart.register_restaurant("Food Court-2", "BTM", "Burger", 120, 3)

    foodkart.login_user("phoneNumber-2")
    foodkart.register_restaurant("Food Court-3", "HSR", "SI Thali", 150, 1)

    foodkart.login_user("phoneNumber-3")
    foodkart.show_restaurants("price")

    foodkart.place_order("Food Court-1", 2)
    foodkart.place_order("Food Court-2", 7)

    foodkart.create_review("Food Court-2", 3, "Good Food")
    foodkart.create_review("Food Court-1", 5, "Nice Food")

    foodkart.show_restaurants("rating")

    foodkart.login_user("phoneNumber-1")
    foodkart.update_quantity("Food Court-2", 5)

    foodkart.update_location("Food Court-2", "BTM/HSR")
