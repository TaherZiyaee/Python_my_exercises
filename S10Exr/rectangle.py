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
        print(f"\nDimensions of the rectangle is:\nWidth: {self.width} , Length: {self.length}")

    def get_dimensions(self) -> None:
        dimens = list(map(float,input("Please enter width and length of the rectangle (ex: 7,4): ").split(',')))
        width=dimens[0]
        length=dimens[1]
        self.move(width, length)


rectangle = None


def get_rec():
    global rectangle
    if not rectangle:
        rectangle = Rectangle()
    return rectangle


def main():
    rec = get_rec()
    rec.get_dimensions()
    rec.show_rectangle()


if __name__ == "__main__":
    main()

