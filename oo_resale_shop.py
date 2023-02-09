from computer import *
class ResaleShop:

    # What attributes will it need?
    inventory: list
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, inventory: list):
        self.inventory = [] # You'll remove this when you fill out your constructor

    # What methods will you need?
    def add_to_inventory(self, computer): #add computer to inventory list
        self.inventory.append(computer)

    def remove_from_inventory(self, computer): #remove computer form inventory list
        if computer in self.inventory: 
            self.inventory.remove(computer)
        else: 
            print("Computer not found.")

    def price_update(self, computer, new_price): #update computer price
        if computer in self.inventory: 
            computer.price = new_price 
        else: 
            print("Computer not found.")

    def operating_system_update(self, computer, newOS): #update computer operating system in inventory 
        if computer in self.inventory:
            computer.operating_system = newOS
        else: 
            print("Computer not found")

    def refurbish_computer(self, computer, newOS): #refurbish computer based on year made
        if computer in self.inventory: 
            if int(computer.year_made) < 2000:
                computer.price = 0 #too old to resell
            elif int(computer.year_made) < 2012: 
                computer.price = 250 # heavily-discounted price on machines 10+ years old
            elif int(computer.year_made) < 2018: 
                computer.price = 550 # discounted price on machines 4-to-10 year old machines
            else: 
                computer.price = 1000 #recent computers
            if newOS is not None: 
                computer.operating_system = newOS #update operating system OS
        else: 
            print("Computer not found")

def main():
    pass
