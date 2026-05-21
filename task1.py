print("welcome to the pattern generator and number analyzer program")
while True:
    print("select any option")
    print("0. exit")
    print("1. pattern generator")
    print("2. number analyzer")
    n = int(input("Enter any option: "))
    match n:
        case 0:
            print("exit")
            break

        case 1:
            a = int(input("enter value."))
            x = a
            for i in range(1, x + 1):
                for j in range(1, i + 1):
                    print("*", end="")
                print("")

        case 2:
            first = int(input("enter start value : "))
            last = int(input("enter last value : "))
            sum = 0
            for i in range(first, last + 1):
                if i % 2 == 0:
                    print(i, " is even")
                else:
                    print(i, " is odd")
                sum = sum + i
            print("sum of all values is", sum)
            print("")

        case _:
            print("invalid input")
