class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print("The Restaurant is open")

    def set_number_served(self, number):
        self.number_served = number
        print("Total customers served by this restaurant are " + str(self.number_served))

    def increment_number_served(self, no_of_customers):
        self.number_served += 100

restaurant1 = Restaurant('Family In', 'Cholle Bathure')
restaurant2 = Restaurant('Midtown', 'Paneer')
restaurant3 = Restaurant('Haldi', 'Bhuna Chicken')

def print_for_restaurant(o):
    o.describe_restaurant()

print_for_restaurant(restaurant1)
print_for_restaurant(restaurant2)
print_for_restaurant(restaurant3)