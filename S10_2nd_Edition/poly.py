# print('t' + 'z')
# print(3 + 8)
# print(4 + 2j + 5j)

# ------------------

class Cat:
    def __init__(self, name: str = "", color: str = None) -> None:
        self.name = name
        self.color = color

    def __str__(self) -> str:
        print('-' * 20)
        return f"Name : {self.name}\nColor: {self.color}"


cat1 = Cat("Moka")
cat2 = Cat("Chapman","Black & White")
print(cat1)
print(cat2)
