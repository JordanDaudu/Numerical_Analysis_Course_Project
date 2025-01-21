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
    print("You have chosen Defect Prediction based on LOC.")
    x = float(input("Enter the value of x: "))
    y = float(input("Enter the value of y: "))
    LOC = float(input("Enter the value of LOC: "))
    result1 = defect_prediction(x, y, LOC)
    print(f"\nDefect Prediction based on LOC: {result1}")
if all or choice == 2:
    print("You have chosen Halstead's Defect Model.")
    v = float(input("Enter the value of v: "))
    result2 = halstead_defect_prediction(v)
    print(f"\nHalstead's Defect Model: {result2}")
if all or choice == 3:
    print("You have chosen Lipow’s Defect Model.")
    A0 = float(input("Enter the value of A0: "))
    A1 = float(input("Enter the value of A1: "))
    A2 = float(input("Enter the value of A2: "))
    LOC = float(input("Enter the value of LOC: "))
    result3 = lipow_defect_prediction(A0, A1, A2, LOC)
    print(f"\nLipow’s Defect Model: {result3}")
if all or choice == 4:
    print("You have chosen Gaffney's Model for Optimal Module Size.")
    a = float(input("Enter the value of a: "))
    b = float(input("Enter the value of b: "))
    LOC = float(input("Enter the value of LOC: "))
    result4 = gaffney_defect_prediction(a, b, LOC)
    print(f"\nGaffney's Model for Optimal Module Size: {result4}")
if all or choice == 5:
    print("You have chosen Goldilock’s Conjecture Polynomial Regression.")
    a = float(input("Enter the value of a: "))
    b = float(input("Enter the value of b: "))
    c = float(input("Enter the value of c: "))
    LOC = float(input("Enter the value of LOC: "))
    result5 = goldilocks_defect_prediction(a, b, c, LOC)
    print(f"\nGoldilock’s Conjecture Polynomial Regression: {result5}")
if all:
    print("================================================================================")
    print("Results:")
    linear = (result1 + result2) / 2
    quadratic = (result3 + result4 + result5) / 3
    print(f"Linear Prediction: {linear}")
    print(f"Quadratic Prediction: {quadratic}")
    print("The difference between the two predictions is:", abs(linear - quadratic))