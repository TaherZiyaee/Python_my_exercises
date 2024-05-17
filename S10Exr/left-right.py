class BaseClass():
    num_base_calls = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def call_me(self):
        print("Calling method on BaseClass.")
        self.num_base_calls += 1


class LeftSubClass(BaseClass):
    num_left_calls = 0

    def __init__(self, c, **kwargs):
        super().__init__(**kwargs)
        self.c = c

    def call_me(self):
        super().call_me()
        print("Calling method on LeftSubClass.")
        self.num_left_calls += 1


class RightSubClass(BaseClass):
    num_right_calls = 0

    def __init__(self, d, e, f, **kwargs):
        super().__init__(**kwargs)
        self.d = d
        self.e = e
        self.f = f

    def call_me(self):
        super().call_me()
        print("Calling method on RightSubClass.")
        self.num_right_calls += 1


class SubClass(LeftSubClass, RightSubClass):
    num_sub_calls = 0

    def __init__(self, g, **kwargs):
        super().__init__(**kwargs)
        self.g = g

    def call_me(self):
        super().call_me()
        print("Calling method on SubClass.")
        self.num_sub_calls += 1


# s = BaseClass(2, 5)
# s = LeftSubClass(a=2,b=5,c=3)
# s = RightSubClass(d=2,e=4,f=6,a=1,b=3)
s = SubClass(d=2, e=4, f=6, a=1, b=3, g=10, c=5)
s.call_me()
# print(s.num_base_calls,s.num_left_calls)
print(s.num_base_calls, s.num_right_calls, s.num_left_calls, s.num_sub_calls)
print(s.a, s.b, s.f, s.e, s.d, s.g, s.c)
