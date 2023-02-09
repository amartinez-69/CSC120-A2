class Computer:

    # What attributes will it need?
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    price: int
    year_made: int
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description: str, processor_type: str, hard_drive_capacity: int, memory: int, operating_system: str, price: int, year_made: int):
        self.description = description 
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.price = price # You'll remove this when you fill out your constructor
        self.year_made = year_made
    # What methods will you need?
    def printDetails(self): 
        print(self.description)
        print(self.processor_type)
        print(self.hard_drive_capacity)
        print(self.memory)
        print(self.operating_system)
        print(self.price)
        print(self.year_made)

def main():
    myComputer = Computer("MacBook Pro", "M1", 1000, 16, "MacOS", 1099, 2021)
    myComputer.printDetails()

main()