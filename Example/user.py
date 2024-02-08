from pprint import pprint


class User:
    all_users = []

    def __init__(self, username: str, password: str, email: str) -> None:
        self.username = username
        self.email = email
        self.password = password
        User.all_users.append(self)

    def __str__(self):
            return f"{self.username}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.username!r},{self.password!r},{self.email!r})"


class Seller(User):
    def order(self, order:"Order")->None:
        print(f"{self.username}, From your products {order!r} was sold!")

def main():
    # print(User.__base__)
    user1 = User("Taher", "123456", "Tahez@gmail.com")
    # user2 = User("Saeid", "111111", "SaeidR@gmail.com")
    # pprint(User.all_users)
    # print(User.all_users)

    print(Seller.__base__)
    s1=Seller("Afshin","4214","afshinKH@gmail.com")
    print(Seller.all_users)
    print(s1)
    print(repr(s1))
    s1.order("book")
    print(s1.all_users)


if __name__ == "__main__":
    main()
