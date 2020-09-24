# Tom Rietjens
# Credit Pset

INVALID = -1

# ========================= Validation Subroutines =======================

def validateFormat(cardNum):
    """checks a string of numbers separated by spaces if it is 16 numbers long
       and if its made up of single digits of integers

    Args:
        cardNum (String): numbers separated by 

    Returns:
        [int]: formated to be used by other subroutines
        (boolean): True if valid, False if not
    """ 
    cardNum = list(cardNum.strip())
    if len(cardNum) != 16:
        print("Card isn't 16 digits:", len(cardNum), "digits")
        return None, False
    for i in cardNum:
        try:
            int(i)
        except:
            print("not all elements are numbers")
            return None, False
    cardNum = [int(i) for i in cardNum]
    return cardNum, True

def validateCardNumber(cardNum):
    """checks if the card number is valid based on Luhn's algorithm

    Args:
        cardNum (List of int): Card number to be checked (in correct format already)

    Returns:
        Bool: returns True if valid based on Luhn's algorithm, False if not
    """

    everySecondNum = []
    for i in range(0,len(cardNum)//2):  # 'unzips' the list
        digit = cardNum.pop(i)
        everySecondNum.append(digit)
    
    sumESN = 0
    for i in everySecondNum:
        ix2 = i*2
        if len(str(ix2)) > 1:
            sumESN += int(str(ix2)[0]) + int(str(ix2)[1]) # if its a 2 digit number, it adds the two digits seperatly
        else:
            sumESN += ix2
    
    total = sumESN + sum(cardNum)
    if str(total)[-1] == "0":
        return True
    else:
        return False

def validatePath(path):
    try:
        fileHandle = open(path,"r")
    except:
        return False
    fileHandle.close()
    return True

# ========================= Subroutines for the 3 options ================

def checkCard():
    """Called from the main subroutine
        User input for card numbers
        Input validation and then correct formatting
        card Number validation using Luhn's algorithm
        Prints appropriate message if valid or invalid
    """
    cardNum = input("\nPlease enter your 16 digit card number in one go (16 digits, no spaces):\n")
    cardNum, validFormat = validateFormat(cardNum)
    if validFormat:
        if validateCardNumber(cardNum):
            print("The card Number is valid! ")
        else:
            print("the card Number is invalid...")


def checkImportNum():
    """Called from the main subroutine
        User inputs the path to the file
        inputted path is validated
        file is opened and contents are traversed line by line
        for each line:
            format is validated
            card number is validated using Luhn's algorithm
            appropriate message printed
    """
    path = input("\ninput the relative path of the file:")
    if validatePath(path):
        with open(path,"r") as f:
            for line in f:
                cardNum, validFormat = validateFormat(line.strip())
                if validFormat:
                    if validateCardNumber(cardNum):
                        print("The card Number: ", line.strip()," is valid! ")
                    else:
                        print("the card Number: ", line.strip()," is invalid...")
        f.close()
    else:
        print("Invalid path")

                        



def generateCC():
    pass


# ========================= Menu and main Program ========================
def menu():
    """Displays the menu for the user

    Returns:
        (int): valid user input
    """
    print("\n\nOptions:")
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
    """Main subroutine
        calls subroutines according to users choice

    Args:
        ans (int): users choice, subrouting called accordingly

    Returns:
        (Bool): False to quit the main loop
    """
    if ans == 1:
        checkCard()
    elif ans == 2:
        checkImportNum()
    elif ans == 3:
        generateCC()
    else:
        print("Thank you\n")
        return False
    return True






go = True
while go:
    # Could just do: go = main(menu()) but for clarity:
    chosen = menu()
    go = main(chosen)


# testCardNum = "0378282246310005"
# num, boo = validateFormat(testCardNum)
# print(validateCardNumber(num))

# checkImportNum()

# Path specific to me:
# /Users/Tom/Desktop/CS-A-Level/MWDCredit.txt