###########################################################11111111111##################################################
import sys
counter = 0


def starter():
    choice = input("type 1 to add a number or something else to terminate:\t")
    return choice


def EvenOdd():
    global counter
    try:
        numb = int(input(""))
        if numb % 2 == 0:
            counter += 1
    except ValueError:
        print("add a number please")


def termination():
    print(f"{counter} even numbers were added")
    sys.exit()


def main():
    choice = starter()
    if choice == '1':
        EvenOdd()
    else:
        termination()


if __name__ == "__main__":
    while True:
        main()

###########################################################22222222222##################################################
counter = 0


def starter():
    choice = input("type 1 to add a number or something else to terminate:\t")
    return choice


def EvenOdd():
    global counter
    try:
        numb = int(input(""))
        if numb % 2 == 0:
            counter += 1
    except ValueError:
        print("add a number please")


def termination():
    print(f"{counter} even numbers were added")


def main():
    choice = starter()
    if choice == '1':
        EvenOdd()
    else:
        termination()
        return False


if __name__ == "__main__":
    while main() != False:
        main()
###########################################################33333333333##################################################
counter = 0


def starter():
    choice = input("type 1 to add a number or something else to terminate:\t")
    return choice


def EvenOdd():
    global counter
    try:
        numb = int(input(""))
        if numb % 2 == 0:
            counter += 1
    except ValueError:
        print("add a number please")


def termination():
    print(f"{counter} even numbers were added")


def main():
    while True:
        choice = starter()
        if choice == '1':
            EvenOdd()
        else:
            termination()
            break


if __name__ == "__main__":
    main()


