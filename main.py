from math import log
# 1.Defect prediction based on LOC
def defect_prediction(x, y, l):
    return x + y * l

# 2.Halstead's defect model
def halstead_defect_prediction(v):
    return v / 3000

# 3.Lipow’s defect model
def lipow_defect_prediction(A0, A1, A2, l):
    return A0 + A1 * log(l) + A2 * (log(l)) ** 2

# 4.Gaffney's Model for Optimal Module Size
def gaffney_defect_prediction(a, b, c, l):
    return a + b * l + c * (l ** 4/3)

# 5.Goldilock’s Conjecture Polynomial Regression
def goldilocks_defect_prediction(a, b, c, l):
    return a + b * l + c * (l ** 2)

