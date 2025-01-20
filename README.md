# Numerical Analysis Course Project

This repository contains the final project for a numerical analysis course, which covers various numerical methods implemented in Python. The project leverages formulas and concepts discussed in the paper _A Critique of Software Defect Prediction Models_ by Norman E. Fenton and Martin Neil, specifically focusing on prediction using size and complexity metrics.

## Table of Contents

- [About](#about)
- [Features](#features)
- [Project Structure](#project-structure)
- [Formulas Used](#formulas-used)

## About

The project demonstrates formulas that are implemented for software defect prediction based on the referenced paper, we are using Numericals methods as well to get variables from the data provided for the project

## Features

- Software defect prediction formulas
- Numerical integration methods
- Cubic spline interpolation
- Finding roots of equations
- Jacobi and Gauss-Seidel iterative methods
- Lagrange and Neville interpolation
- Linear and polynomial interpolation

## Project Structure

```
Numerical_Analysis_Course_Project/
│-- colors.py
│-- cubic_Spline_interpolation.py
│-- finding_roots_of_equations.py
│-- jacobi_and_gauss_seidel_iterative_methods.py
│-- lagrange_and_neville_interpolation.py
│-- linear_and_polynomial_interpolation.py
│-- main.py
│-- .gitignore
│-- LICENSE
│-- README.md
```

## Formulas Used

The following formulas are implemented in `main.py` for software defect prediction based on the referenced paper:

1. **Defect Prediction Based on LOC** <br>
   D = x + y * LOC

2. **Halstead's Defect Model**<br>
   D = v / 3000

3. **Lipow’s Defect Model**<br>
   D = A0 + A1 * log(LOC) + A2 * (log(LOC))^2

4. **Gaffney's Model for Optimal Module Size**<br>
   D = a + b * (LOC^(4/3))

5. **Goldilock’s Conjecture Polynomial Regression**<br>
   D = a + b * LOC + c * LOC^2


These formulas are used to estimate software defects based on size and complexity metrics.

