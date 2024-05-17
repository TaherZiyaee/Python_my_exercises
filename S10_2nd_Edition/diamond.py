from datetime import datetime
class Person:
    def __init__(self,name:str="",sex:str=""):
        self.__name=name
        self.__sex=sex
        self.birthday:datetime=None



    def get_name(self):
        return self.__name

    def set_name(self,name:str):
        if not name.isalpha():
            raise "A person's name can only contain letters!"
        else:
            self.__name=name

    def set_sex(self,sex:str):
        if not (sex=='M' or sex=='F'):
            raise "Sex property must be 'M' of 'F'!"
        else:
            self.__sex=sex

    def __repr__(self):
        return f"{self.__class__.__name__}({self.get_name()}, {self.__sex})"



class Student(Person):
    def __init__(self):
        super().__init__()
        self.address:str=""
        self.department:str=""

class Teacher(Person):
    def __init__(self):
        super().__init__()
        self.rank=0
        self.courseInfo=list()

def main():
    prs1=Person()
    prs1.set_name("Taher Ziyaee")
    prs1.set_sex("M")

    print(prs1)

if __name__=="__main__":
    main()