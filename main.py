import math

def function1(x):
    return (x ** 3) - (6 * x ** 2) + (12 * x) - 8


def function2(x):
    return math.tan(x) - 2 * x


def derivative1(x):
    return (3 * x ** 2) - (12 * x) + 12


def derivative2(x):
    return (1 / (math.cos(x)) ** 2) - 2


initialNewton1 = 1.4
initialNewton2 = 3


# Code base on Wikipedia articles on Newton Method and Bisection Method

# https://en.wikipedia.org/wiki/Newton%27s_method

# https://en.wikipedia.org/wiki/Bisection_method

def bisection_method(func, a, b, tol):
    end_point_a = a
    end_point_b = b
    tolerance = tol
    print("End A: ", end_point_a)
    print("End B: ", end_point_b)
    print("Tolerance: ", tolerance)
    function = func
    if function == 1:
        n = 0
        n_max = 100
        while n < n_max:  # Limits loop to n_max to prevent infinite loops
            n = n + 1
            c = (end_point_a + end_point_b) / 2  # Midpoint is set to variable c
            print(n, c)
            if function2(end_point_a) * function2(end_point_b) > 0: #If the function2 has the same sign each step
                # the interval is not acceptable
                print("Bisection Failed: No root found")

            if function1(c) == 0 or (
                    end_point_b - end_point_a) / 2 < tolerance:  # Function will prints answer if a tolerance is met or
                # the function is zero
                print("Number of Iterations: ", n)
                print("Bisection Guess: ", c)
                break

            if function1(end_point_a) * function1(c) < 0:  # Sets interval depending on where the root is located
                end_point_b = c

            elif function1(end_point_b) * function1(c) > 0:  # Sets interval depending on where the root is located
                end_point_a = c

    if function == 2:
        n = 0
        n_max = 100  # Limits loop to n_max to prevent infinite loops

        if function2(end_point_a) * function2(end_point_b) > 0: #If the function2 has the same sign each step
            #the interval is not acceptable
            print("Bisection Failed: No root found")

        else:
            while (end_point_b - end_point_a) / 2 > tolerance:  # Loop will stop if tolerance is met
                n = n + 1

                c = (end_point_b + end_point_a) / 2  # Midpoint is set to variable c
                print(n, c)
                if function2(c) == 0:  # Function will prints answer function is zero
                    return c

                elif function2(end_point_a) * function2(c) < 0:  # Sets interval depending on where the root is located

                    end_point_b = c

                else:
                    end_point_a = c

                if n == n_max:
                    break
            print("Number of Iterations: ", n)
            print("Bisection Guess: ", c)


def newton_method(initial, tol, func, dir):
    n_max = 100
    xo = initial
    tolerance = tol
    solution_found = 0
    function = func
    print("Initial: ", xo)
    print("Tolerance:", tolerance)

    if function == 1:
        n = 0
        for i in range(1, n_max):  # limits the loop to n_max to prevent infinite loop
            n = n + 1
            y = function1(xo)
            y_prime = derivative1(xo)
            x1 = xo - (y / y_prime)  # Newton formula calculation
            print(i, x1)

            if abs(x1 - xo) <= (tolerance * abs(x1)):  # If the result is inside a tolerance, print solution
                solution_found = 1
                print("Number of Iterations: ", n)
                break
            xo = x1  # Update xo and run the loop again

        if solution_found == 1:
            print("Newton Method Guess:", x1)

        else:
            print("Did not converge")

    if function == 2:
        n = 0
        for i in range(1, n_max):  # limits the loop to n_max to prevent infinite loop
            n = n + 1
            y = function2(xo)
            y_prime = derivative2(xo)
            x1 = xo - (y / y_prime)  # Newton formula calculation
            print(i, x1)

            if abs(x1 - xo) <= (tolerance * abs(x1)):  # If the result is inside a tolerance, print solution
                solution_found = 1
                print("Number of Iterations: ", n)
                break
            xo = x1  # Update xo and run the loop again

        if solution_found == 1:
            print("Newton Method Guess: ", x1)

        else:
            print("Did not converge")


def main():
    function = int(input("What function would you like to use?\n1: x^3 - 6x^2 + 12x -8\n2: tan(x) - 2x\n"))

    method = int(input("What method would you like to use\n 1: Bisection 2: Newton"))

    if method == 1 and function == 1:
        bisection_method(function, 1, 3, 0.0001)

    if method == 1 and function == 2:
        bisection_method(function, 1, 1.4, 0.0001)

    if method == 2 and function == 1:
        select_derivative = 1
        newton_method(3, 0.0001, function, select_derivative)

    if method == 2 and function == 2:
        select_derivative = 2
        newton_method(1.4, 0.0001, function, select_derivative)


main()
