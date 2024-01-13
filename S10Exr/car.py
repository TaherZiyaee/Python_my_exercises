class Car:
    def __init__(self)->None:
        self.brand=brand
        self.model=""
        self.year=""

    def get_car(self)->None:
        print("-- Please enter car specifications --")
        self.brand=input("Brand: ")
        self.model=input("Model: ")
        self.year=input("Year: ")
