from math import log
from colors import bcolors
# 1.Defect prediction based on LOC
def defect_prediction(x, y, LOC):
    return x + y * LOC

# 2.Halstead's defect model
def halstead_defect_prediction(v):
    return v / 3000

# 3.Lipow’s defect model
def lipow_defect_prediction(A0, A1, A2, LOC):
    return A0 + A1 * log(LOC) + A2 * (log(LOC)) ** 2

# 4.Gaffney's Model for Optimal Module Size
def gaffney_defect_prediction(a, b, LOC):
    return a + b * (LOC ** 4/3)

# 5.Goldilock’s Conjecture Polynomial Regression
def goldilocks_defect_prediction(a, b, c, LOC):
    return a + b * LOC + c * (LOC ** 2)

def get_non_negative_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            else:
                print("Error: Value cannot be negative. Please enter 0 or a positive number.")
        except ValueError:
            print("Error: Invalid input. Please enter a numeric value that is positive or 0.")

def get_number_between_0_and_1(prompt):
    while True:
        try:
            value = float(input(prompt))
            if 0 <= value <= 1:
                return value
            else:
                print("Error: Value must be between 0 and 1 (inclusive). Please try again.")
        except ValueError:
            print("Error: Invalid input. Please enter a numeric value between 0 and 1.")

while True:
    print("Please choose the method you want to use:")
    print("1. Defect Prediction based on LOC")
    print("2. Halstead's Defect Model")
    print("3. Lipow’s Defect Model")
    print("4. Gaffney's Model for Optimal Module Size")
    print("5. Goldilock’s Conjecture Polynomial Regression")
    print("6. All of the above")
    try:
        choice = int(input("Enter your choice: "))
        if choice in [1, 2, 3, 4, 5, 6]:
            break
        else:
            print("Invalid choice. Please enter valid choice.")
    except ValueError:
        print("Invalid input. Please enter a number.")
print("================================================================================")
if choice == 6:
    all = True
else:
    all = False
if all or choice == 1:
    print(bcolors.OKCYAN ,"\nYou have chosen Defect Prediction based on LOC.", bcolors.ENDC)
    x = get_non_negative_number("Enter the value of x: ")
    y = get_non_negative_number("Enter the value of y: ")
    LOC = get_non_negative_number("Enter the value of LOC: ")
    result1 = defect_prediction(x, y, LOC)
    print(bcolors.OKGREEN ,f"\nDefect Prediction based on LOC: {result1}", bcolors.ENDC)
if all or choice == 2:
    print(bcolors.OKCYAN ,"\nYou have chosen Halstead's Defect Model.", bcolors.ENDC)
    v = get_non_negative_number("Enter the value of v: ")
    result2 = halstead_defect_prediction(v)
    print(bcolors.OKGREEN ,f"\nHalstead's Defect Model: {result2}", bcolors.ENDC)
if all or choice == 3:
    print(bcolors.OKCYAN ,"\nYou have chosen Lipow’s Defect Model.", bcolors.ENDC)
    A0 = get_number_between_0_and_1("Enter the value of A0: ")
    A1 = get_number_between_0_and_1("Enter the value of A1: ")
    A2 = get_number_between_0_and_1("Enter the value of A2: ")
    LOC = get_non_negative_number("Enter the value of LOC: ")
    result3 = lipow_defect_prediction(A0, A1, A2, LOC)
    print(bcolors.OKGREEN ,f"\nLipow’s Defect Model: {result3}", bcolors.ENDC)
if all or choice == 4:
    print(bcolors.OKCYAN ,"\nYou have chosen Gaffney's Model for Optimal Module Size.", bcolors.ENDC)
    a = get_non_negative_number("Enter the value of a: ")
    b = get_non_negative_number("Enter the value of b: ")
    LOC = get_non_negative_number("Enter the value of LOC: ")
    result4 = gaffney_defect_prediction(a, b, LOC)
    print(bcolors.OKGREEN ,f"\nGaffney's Model for Optimal Module Size: {result4}", bcolors.ENDC)
if all or choice == 5:
    print(bcolors.OKCYAN ,"\nYou have chosen Goldilock’s Conjecture Polynomial Regression.", bcolors.ENDC)
    a = get_non_negative_number("Enter the value of a: ")
    b = get_non_negative_number("Enter the value of b: ")
    c = get_non_negative_number("Enter the value of c: ")
    LOC = get_non_negative_number("Enter the value of LOC: ")
    result5 = goldilocks_defect_prediction(a, b, c, LOC)
    print(bcolors.OKGREEN ,f"\nGoldilock’s Conjecture Polynomial Regression: {result5}", bcolors.ENDC)
if all:
    print("================================================================================")
    print(bcolors.GOLD ,"\nResults:", bcolors.ENDC)
    linear = (result1 + result2) / 2
    quadratic = (result3 + result4 + result5) / 3
    print(bcolors.OKBLUE ,f"\nLinear Prediction: {linear}")
    print(f"Quadratic Prediction: {quadratic}", bcolors.ENDC)
    print(bcolors.OKGREEN ,"\nThe difference between the two predictions is:", abs(linear - quadratic), bcolors.ENDC)