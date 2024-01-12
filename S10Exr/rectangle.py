class Rectangle:
    def __init__(self, width: float = 0, length: float = 0) -> None:
        self.move(width, length)

    def move(self, width: float, length: float) -> None:
        self.width = width
        self.length = length

    def reset(self) -> None:
        self.move(0, 0)

    def perimeter(self) -> float:
        return (self.length + self.width) * 2

    def area(self) -> float:
        return self.length * self.width

    def show_rectangle(self) -> None:
        print(f"Dimensions of the rectangle is:\nLength: {self.length} , Width: {self.width}")

    def get_dimensions(self, width: float = 0, length: float = 0) -> None:
        # length, width = float(input("Please enter length and width of the rectangle (ex: 7,4): ").split(','))
        width = float(input("Please enter length and width of the rectangle (ex: 7,4): "))
        self.move(width, length)


rectangle = None


def get_rec():
    global rectangle
    if not rectangle:
        rectangle = Rectangle
    return rectangle


def main():
    rec = get_rec()
    rec.get_dimensions(5,7)
    rec.show_rectangle()


if __name__ == "__main__":
    main()
