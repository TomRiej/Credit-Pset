# Tom Rietjens
# Credit Pset

INVALID = -1

def menu():
    print("Options:")
    print("1. Check my card")
    print("2. Import numbers to check")
    print("3. Generate a valid CC number")
    print("4. Quit")
    valid = False
    while not valid:
        try:
            ans = int(input("enter the number you want to choose: "))
        except:
            ans = INVALID
        if ans in range(1,5):
            valid = True
        else:
            print("invalid input: must be integer from 1-4\n")
    return ans

def main(ans):
    if ans == 1:
        checkCard()
    elif ans == 2:
        checkImportNum()
    elif ans == 3:
        generateCC()
    else:
        print("Thank you\n")


def validateFormat(cardNum):
    cardNum = cardNum.strip().split(" ")
    if len(cardNum) != 16:
        print("Card isn't 16 digits:", len(cardNum), "digits")
        return False
    for i in cardNum:
        if len(i) > 1:
            print("not all elements are single digit numbers (0-9)")
            return False
        try:
            int(i)
        except:
            print("not all elements are numbers")
            return False
    cardNum = [int(i) for i in cardNum]
    return cardNum, True


def checkCard():
    cardNum = input("Please enter your 16 digit card number separated by spaces:\n")
    cardNum, validFormat = validateFormat(cardNum)
    if validFormat:
        pass






def checkImportNum():
    pass

def generateCC():
    pass


# Could just do: main(menu()) but for clarity:
chosen = menu()
main(chosen)


# testCardNum = "0 3 7 8 2 8 2 2 4 6 3 1 0 0 0 5"
# validateFormat(testCardNum)
