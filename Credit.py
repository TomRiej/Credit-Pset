# Tom Rietjens
# Credit Pset

from random import randint

CARD_LENGTH = 16


# ================= Luhn's algoritm and Validation Subroutines ===========

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

def createValidCC():
    # max : 9999999999999999 => (with luhn alg.) total of 144 ==> highest valid num total is 140
    # min : 0000000000000000 => (with luhn alg.) total of 0  ==> lowest valid sum is 0 

    # Creates every Second number, as these are the ones which undergo luhn alg
    sumMaxSingle = 9*8
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
        
    # created a maximum and minimum valid total number (last digit is 0)
    sumMax = int(str(sumESN + sumMaxSingle)[:-1]) # removes the last digit to make RNG*10 make a valid total (0 at end) 
    sumMin = int(str(sumESN+10)[:-1])             
    total = randint(sumMin,sumMax)*10
    difference = total - sumESN

    # the difference is then made up using random numbers
    # these numbers become the other half of every second number to create a full card number
    unalteredDigits = []
    while len(unalteredDigits) < 8:
        if difference > 0:
            digit = randint(0,9)
            if difference - digit >= 0:
                unalteredDigits.append(digit)
                difference -= digit
        else:
            unalteredDigits.append(0)
    

    # puts both halves of the card number together
    validCardNum = []
    for i in range(CARD_LENGTH//2):
        validCardNum.append(eSN[i])
        validCardNum.append(unalteredDigits[i])
    return "".join([str(i) for i in validCardNum])
    
    



    
    

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

    for i in range(0,quantity):
        validCardNum = createValidCC()
        #  Tests:
        # tempCardNum, boo = validateFormat(validCardNum)
        # print(validCardNum,"Format: ",boo,"Number:", validateCardNumber(tempCardNum))



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
            ans = False
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
        confirm = input("Are you sure you want to quit? 'n': ")
        if confirm == "n":
            return True
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