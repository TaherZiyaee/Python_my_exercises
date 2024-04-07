from pprint import pprint


class UserList(list["User"]):
    def search(self, user_name: str) -> list["User"]:
        matching_users: list["User"] = []
        for user in self:
            if user_name in user.username:
                matching_users.append(user)
        return matching_users


class User:
    # all_users = []
    all_users = UserList()

    def __init__(self, username: str, password: str, email: str) -> None:
        self.username = username
        self.email = email
        self.password = password
        User.all_users.append(self)

    def __str__(self) -> str:
        return f"{self.username}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.username!r},{self.password!r},{self.email!r})"


class Seller(User):
    def order(self, order: "Order") -> None:
        print(f"{self.username}, From your products {order!r} was sold!")


class Buyer(User):
    def __init__(self, username: str, email: str, password: str, phone: str):
        super().__init__(username, email, password)
        self.phone = phone

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.username!r},{self.password!r},{self.email!r}," \
               f"{self.phone})"


def main():
    # print(User.__base__)
    user1 = User("Taher", "123456", "Tahez@gmail.com")
    user2 = User("Saeid", "111111", "SaeidR@gmail.com")
    user3 = User("reza", "8710301", "reza@gmail.com")
    user4 = User("ali", "809123", "aliM@gmail.com")
    user5 = User("alireza", "25435", "alirezaS@gmail.com")
    # pprint(User.all_users)
    # print(User.all_users)

    # print(Seller.__base__)
    # s1=Seller("Afshin","4214","afshinKH@gmail.com")
    # print(Seller.all_users)
    # print(s1)
    # print(repr(s1))
    # s1.order("book")
    # print(s1.all_users)

    # pprint(User.all_users.search("reza"))

    buyer_account = Buyer("reza","reza34@yahoo.com","2143","0939")
    # print(buyer_account.phone)
    # pprint(buyer_account.all_users)

    print(isinstance(buyer_account,User))


if __name__ == "__main__":
    main()
