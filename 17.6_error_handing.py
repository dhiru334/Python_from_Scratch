while True:
    try:
        a = int(input("Enter number 1:"))
        b = int(input("Enter number 2:"))

        print(f"The division  is {a/b}")
    except ValueError:
        print("Please dont division by 0")
    except Exception as e:
        print("Hey dont divide by 0")
    except Exception as e:
        print("Some error occured!", e)