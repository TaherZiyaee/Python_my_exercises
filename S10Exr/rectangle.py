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

rectangle=None
def get_rec():
    global rectangle
    if not rectangle:
        rectangle=Rectangle
    return rectangle

def main():
    ...