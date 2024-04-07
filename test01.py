x = 17.76325687236
y = 4

# print("pow is",pow(x,y))
# print("divmod is",divmod(x,y))
# print("round is",round(x,y))
# print("integer ratio is",x.as_integer_ratio())
# print(x.is_integer())

# for method in dir(dict):
#     print(method)

# sentence="Hello Baby CommOn\nwHats youR nAMe?"
# print(sentence.casefold())
# print(sentence.title())
# print(sentence.partition("CommOn"))

# name="Taher"
# print(name.center(len(name)+2," ").center(len(name)+10,"-"))

# lst = [
#     ["a", "dsffsdfs", "sdf"],
#     ["dsfsd", "df", "jhsgdfjhgsd"]
# ]
#
# for name in lst:
#     print("{: >20}{: >20}".format(*name))


# print("%*s\t\t%i" % (15,"Ali",17))

# ----------------------------------------
class SuperClass1:
    def print1(self):
        print(self)

class SuperClass2:
    def print2(self):
        print(self)

class SubClass1(SuperClass1,SuperClass2):
    pass

obj = SubClass1()
obj.print1()
obj.print2()