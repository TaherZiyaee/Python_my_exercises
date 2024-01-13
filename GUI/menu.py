from colorama import Fore
from S10Exr.rectangle import get_rec

print()


def main_menu():
    star = '*' * 15
    press_continue="Press any key to continue..."

    # ------- 1. RECTANGLE MENU -------
    def rectangle_menu():
        def print_rectangle_menu():
            print(star,Fore.LIGHTBLUE_EX, "RECTANGLE MENU",Fore.RESET, star)
            print("\t1. Show Rectangle")
            print("\t2. Get Dimensions")
            print("\t3. Perimeter")
            print("\t4. Area")
            print("\t5. Back to MAIN MENU")
            print("\t6. Exit")

        while True:
            print_rectangle_menu()
            choice = input("Enter your choice [1-4]: ")

            rec = get_rec()
            if choice == '1':
                rec.show_rectangle()
                input(press_continue)
            elif choice == '2':
                rec.get_dimensions()
                rec.show_rectangle()
                input(press_continue)
            elif choice == '3':
                rec.show_rectangle()
                print(f"Perimeter of the rectangle ((w+l)*2): {rec.perimeter()}")
                input(press_continue)
            elif choice == '4':
                rec.show_rectangle()
                print(f"Area of the rectangle (w*l): {rec.area()}")
                input(press_continue)
            elif choice == '5':
                return
            elif choice == '6':
                exit(14)
            else:
                print(Fore.RED, "Wrong menu selection! Enter any key to try again ...", Fore.RESET)

            print()

    # ------- 2. CAR MENU -------
    def car_menu():
        def print_car_menu():
            pass

    # ------- 3. STUDENT MENU -------
    def student_menu():
        def print_student_menu():
            pass

    # ------- MAIN MENU -------
    def print_main_menu():
        print(star, Fore.LIGHTBLUE_EX,"MAIN MENU",Fore.RESET, star)
        print("\t1. Rectangle")
        print("\t2. Car")
        print("\t3. Student")
        print("\t4. Exit")

    while True:
        print_main_menu()
        choice = input("Enter your choice [1-4]: ")

        if choice == '1':
            rectangle_menu()
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            exit(13)
        else:
            print(Fore.RED, "Wrong menu selection! Enter any key to try again ...", Fore.RESET)

        print()


main_menu()

# print()
