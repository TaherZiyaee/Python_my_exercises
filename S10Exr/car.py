class Car:
    def __init__(self,brand:str,model:str)->None:
        self.brand=brand
        self.model=""
        self.year=""

    def get_car_specs(self)->None:
        print("-- Please enter car specifications --")
        self.brand=input("Brand: ")
        self.model=input("Model: ")
        self.year=input("Year: ")

car=None
def get_car()->Car:
    global car
    if not car:
        car=Car()
    return car

def main():
    pass

if __name__=="__main__":
    main()