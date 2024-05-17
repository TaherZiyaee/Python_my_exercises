while True:
    try:
        a = int(input("A: "))
        b = int(input("B: "))
        print("A / B =", a / b)
        break
    except ZeroDivisionError:
        print("'B' can not be zero!!")
    except ValueError:
        print("Please enter only digit value!")
    print('-' * 20)

print("End.")

