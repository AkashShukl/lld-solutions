class FoodItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

# used startegy pattern for different ways of sorting
class RestaurantSortStrategy:
    def sort(self, restaurants):
        pass


class RatingSortStrategy(RestaurantSortStrategy):
    def sort(self, restaurants):
        return sorted(restaurants, key=lambda r: r.rating, reverse=True)


class PriceSortStrategy(RestaurantSortStrategy):
    def sort(self, restaurants):
        return sorted(restaurants, key=lambda r: r.food_item.price)


class Restaurant:
    def __init__(self, name, serviceable_pincodes, food_item):
        self.name = name
        self.serviceable_pincodes = serviceable_pincodes
        self.food_item = food_item
        self.rating = 0
        self.reviews = []

    def add_review(self, rating, comment):
        self.reviews.append((rating, comment))
        self.update_rating()

    def update_rating(self):
        total_ratings = sum(rating for rating, _ in self.reviews)
        self.rating = total_ratings / len(self.reviews) if self.reviews else 0

    def increase_quantity(self, quantity_to_add):
        self.food_item.quantity += quantity_to_add
