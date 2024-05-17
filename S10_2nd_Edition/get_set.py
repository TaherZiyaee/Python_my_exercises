class BankUser:
    def __init__(self, name: str = "unknown", national_code: str = "---", phone: str = "---"):
        self.__name = name
        self.__national_code = national_code
        self.__phone = phone

    def set_phone(self, phone: str) -> int:
        len_ = len(phone)
        if len(phone) == 11 and phone.isdigit():
            self.__phone = phone
        return len_

    def get_phone(self)->str:
        return self.__phone

    def set_name(self,name):
        if name.isalpha():
            self.__name=name

    def get_name(self):
        return self.__name

# aliAcc=BankUser("Ali Ahmadi",9486712,534543543)
aliAcc = BankUser()

len_=aliAcc.set_phone("45398787563")
aliAcc.set_name("AliAhmadi")

aliPhone = aliAcc.get_phone()
aliName = aliAcc.get_name()

print(f"Phone Lengh: {len_}\n",aliPhone)
print(aliName)

