class Car:
    def __init__(self, brand: str="", model: str="") -> None:
        self.brand = brand
        self.model = model
        self.year = ""

    def get_car_specs(self) -> None:
        print("-- Please enter car specifications --")
        self.brand = input("Brand: ")
        self.model = input("Model: ")
        self.year = input("Year: ")

    def show_car(self)->None:
        print(f"{self.brand} {self.model} - {self.year}")


car = None


def get_car():
    global car
    if not car:
        car = Car()
    return car


def main():
    car = get_car()
    car.get_car_specs()
    car.show_car()


if __name__ == "__main__":
    main()
