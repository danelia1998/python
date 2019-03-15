
def checker(inputing):
    numbers = 0
    uppers = 0
    symbols = 0
    create = open("something.txt","w")
    lenght = 0


    if type(inputing) is type(create):
# rodesac vinmes txt faili shemoaqvs
        for each in inputing.read():
            if each.isupper():
                uppers += 1
            elif each.isdigit():
                numbers += 1
            elif each in "~!@#$%^&*()<_-+=}{|[]\?/:;'>,." :
                symbols += 1
            lenght += 1
        if lenght <= 5:
            print("Lenght of Pass must be min 6!")
        elif uppers == 0:
            print("You must have min 1 upper Letter!")
        elif symbols != 0:
            print("You cant use symbols!")
        elif lenght >= 6 and uppers > 0 and numbers >= 2 and symbols == 0 :
            print("You are WELCOME !")


    elif type(inputing) == type("dato"):
# rodesac vigacas stringi shemoyavs
        inputing.split()
        for each in inputing:
            if each.isupper():
                uppers += 1
            elif each.isdigit():
                numbers += 1
            elif each in "~!@#$%^&*()<_-+=}{|[]\?/:;'>,." :
                symbols += 1
        if len(inputing) < 6:
            print("Lenght of Pass must be min 6!")
        elif uppers == 0:
            print("You must have min 1 upper Letter!")
        elif symbols != 0:
            print("You cant use symbols!")
        elif len(inputing) >= 6 and uppers > 0 and numbers >= 2 and symbols == 0 :
            print("You are WELCOME !")


    elif type(inputing) == type(["dato"]):
# rodesac vinmes listi shemoyavs
        for each in inputing[0]:
            if each.isupper():
                uppers += 1
            elif each.isdigit():
                numbers += 1
            elif each in "~!@#$%^&*()<_-+=}{|[]\?/:;'>,.":
                print("datp")
                symbols += 1
        if len(inputing[0]) < 6:
            print("Lenght of Pass must be min 6!")
        elif uppers == 0:
            print("You must have min 1 upper Letter!")
        elif symbols != 0:
            print("You cant use symbols!")
        elif len(inputing[0]) >= 6 and uppers > 0 and numbers >= 2 and symbols == 0:
            print("You are WELCOME !")
    else:
        print("Unknown file")


def main():
    inputing = ["AmisMagivradSheidzlebaIyosNebismieriRam123"]
    checker(inputing)
if __name__ == '__main__':
    main()
