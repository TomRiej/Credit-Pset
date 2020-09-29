# Tom Rietjens
# Credit Pset

from random import randint

CARD_LENGTH = 16
WRITE_PATH = "/Users/Tom/Desktop/CS-A-Level/CreatedCCs.txt"

# Path specific to me:
# /Users/Tom/Desktop/CS-A-Level/MWDCredit.txt


# ======================= Validation Subroutines =========================

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
    if len(cardNum) != CARD_LENGTH:
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
        cardNum [int]: Card number to be checked (in correct format already)

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
            sumESN += ix2 - 9 # if its a 2 digit number, it adds the sum of the two digits
        else:
            sumESN += ix2
    
    total = sumESN + sum(cardNum)
    if str(total)[-1] == "0": # fix % 10
        return True
    else:
        return False

def validatePath(path):
    """validates path given by user

    Args:
        path (String): The path

    Returns:
        Bool: True if valid
    """
    try:
        fileHandle = open(path,"r")
    except:
        return False
    fileHandle.close()
    return True


# ======================= Decomposition subroutines ======================

def createESN():
    """Creates a random list of 8 numbers which then undergo luhns algorithm

    Returns:
        [int]: list of random integers
        (int): sum of the integers after luhn's algorithm is implemented.
    """
    eSN = []
    sumESN = 0
    for i in range(0,CARD_LENGTH//2):
        digit = randint(0,9)
        eSN.append(digit)
        res = digit*2
        if len(str(res)) > 1:
            sumESN += res - 9 
        else:
            sumESN += res

    return eSN, sumESN

def zipLists(list1, list2):
    """puts 2 lists together

    Args:
        list1 [any]: A list of items, index 0 becomes index 0 in zipped list
        list2 [any]: A list of items, index 0 becomes index 1 in zipped list

    Returns:
        [any]: The final zipped list
    """
    endList = []
    for i in range(CARD_LENGTH//2):
        endList.append(list1[i])
        endList.append(list2[i])
    return endList

def createValidCC():
    """Creates 1 valid card number
    First creates every second number and finds the sum after Luhn's algorithm
    Second creates 7 random digits for the unaltered numbers
    The difference to a valid total is then added as the 8th
    Lastly zips the lists together to get valid card number.

    Returns:
        (String): The valid card number.
    """

    # Creating a random 8 numbers and finding the result after Luhn's algorithm
    eSN, sumESN = createESN()

    # Creatign another 7 random numbers (unaltered digits in Luhn's algorithm)
    uAN = [randint(0,9) for i in range(CARD_LENGTH//2-1)]

    total = sum(uAN) + sumESN
    rtotal = round((total+5)/10)*10 # rounding up to nearest 10
    difference = rtotal - total
    if difference != 10:
        uAN.append(difference)
    else:
        uAN.append(0)
    
    # puts both halves of the card number together
    validCardNum = zipLists(eSN, uAN)
    validCardNum = "".join([str(i) for i in validCardNum])
    return validCardNum


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
    """Generates x amount of valid, unduplicated credit card numbers
    asks and validates for the quantity of numbers the user wants.
    Writes the created numbers into a file at a specified location
    """
    valid = False
    while not valid:
        try:
            quantity = int(input("\nHow many card numbers do you want? 1-100 "))
            if quantity in range(1,101):
                valid = True
            else:
                print("Invid input: must be 1-100")
        except:
            print("Invalid input: must be a number from 1-100")

    madeNumbers = []
    while len(madeNumbers) < quantity:
        newNum = createValidCC()
        if newNum not in madeNumbers:
            madeNumbers.append(newNum)
        else:
            print(madeNumbers,"\nduplicate:",newNum)
    
    with open(WRITE_PATH, "w") as f:
        for i in madeNumbers:
            print(i)
            f.write(i+"\n")
    f.close()
    print("Numbers written to file at:", WRITE_PATH)


# ========================= Menu and main Program ========================
def menu():
    """Shows the menu to the user

    Returns:
        int: the users choice
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
            ans = False
        if ans in range(1,5):
            valid = True
        else:
            print("invalid input: must be integer from 1-4\n")
    return ans

def pickFunc(ans):
    """Calls the function corresponding to the users input

    Args:
        ans (int): the users choice

    Returns:
        bool: True to continue the program, False to end the 'go' while loop
    """
    if ans == 1:
        checkCard()
    elif ans == 2:
        checkImportNum()
    elif ans == 3:
        generateCC()
    else:
        confirm = input("Are you sure you want to quit? 'n': ")
        if confirm == "n":
            return True
        else:
            print("Thank you\n")
            return False
    return True

def main():
    """Everything should run through here: the main program
    """
    go = True
    while go:
        # could do go = pickFunc(menu()) but for simplicity:
        chosen = menu()
        go = pickFunc(chosen)


# ========================================================================

if __name__ == "__main__":
    main()