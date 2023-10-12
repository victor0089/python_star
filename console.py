#!/usr/bin/python3
class Property:
    def __init__(self, name, location, price, availability):
        self.name = name
        self.location = location
        self.price = price
        self.availability = availability

class AirbnbConsole:
    def __init__(self):
        self.properties = []

    def add_property(self, property):
        self.properties.append(property)

    def display_properties(self):
        print("Available Properties:")
        for i, property in enumerate(self.properties, start=1):
            print(f"{i}. {property.name} - {property.location} - ${property.price} per night")

    def book_property(self, property_index):
        if 1 <= property_index <= len(self.properties):
            property = self.properties[property_index - 1]
            if property.availability:
                property.availability = False
                print(f"Successfully booked {property.name} in {property.location}!")
            else:
                print("Property is not available for booking.")
        else:
            print("Invalid property index.")

# Test the AirbnbConsole
airbnb = AirbnbConsole()

# Adding sample properties
property1 = Property("Cozy Cottage", "Mountain View", 100, True)
property2 = Property("Luxury Villa", "Beachfront", 500, True)
property3 = Property("City Apartment", "Downtown", 200, False)

airbnb.add_property(property1)
airbnb.add_property(property2)
airbnb.add_property(property3)

# Display available properties
airbnb.display_properties()

# Book a property
property_index = int(input("Enter the property index to book: "))
airbnb.book_property(property_index)
