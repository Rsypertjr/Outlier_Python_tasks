
from pydoc import synopsis
from sympy import *

def Secant(expr,X0,X1,iter,eps):
    x=symbols('x')
    xi=X1
    xio=X0
    errs=[]
    app_root=[]
    i=0
    while i < iter:
        # Calculate the function values at x0 and x1
        fx1 = expr.subs(x,xi).evalf()
        fx0 = expr.subs(x,xio).evalf()
        
        # Calculate the next approximation using the secant formula
        x_new = xi - fx1*((xi-xio)/(fx1-fx0))

        # Check for convergence of secant formula
        err=abs((x_new-xi)/x_new)

        # Keep running storage of approximated root and error level
        errs.append(err)
        app_root.append(x_new)

        # Update the values for the next iteration
        xio=xi
        xi=x_new

        # Return when error is less than prescribed by eps argument
        if err < eps:
            break
        i = i+1
    return app_root,errs

x = symbols('x')
expr = x**3 - 2*x - 5
X0 = 2
X1 = 3
iter = 10
eps = 0.0001
app_root, errs = Secant(expr, X0, X1, iter, eps)

print(f"Approximate root: {app_root[-1]}")
print(f"Error: {errs[-1]}")


# Use case 2
expr2 = x**2 - 5
X0_2 = 2
X1_2 = 3
iter2 = 5
eps2 = 0.01
app_root2, errs2 = Secant(expr2, X0_2, X1_2, iter2, eps2)
print("\nUse Case 2:")
print("Approximate Root:", app_root2[-1])
print("Error:", errs2[-1])

# Use case that generates an error (division by zero)
expr3 = x**2 
X0_3 = 2
X1_3 = -2
iter3 = 10
eps3 = 0.0001

try:
    app_root3, errs3 = Secant(expr3, X0_3, X1_3, iter3, eps3)
    print("\nUse Case 3 (Error Case):")
    print("Approximate Root:", app_root3[-1])
    print("Error:", errs3[-1])
except ValueError as e:
    print("\nUse Case 3 (Error Case):")
    print("Error:", e) 