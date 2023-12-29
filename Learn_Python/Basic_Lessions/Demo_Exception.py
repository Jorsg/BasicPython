def functionexception():
    try:
        a= 10
        b=20
        print(a/b)
    except ZeroDivisionError:
        print("There is a division by zero")
    finally:
        print("This is no execute no matter what")

functionexception()