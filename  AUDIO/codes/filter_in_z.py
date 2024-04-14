import sympy as sp

# Define symbols
s, z = sp.symbols('s z')

# Given transfer function
Ha_BP_s = 6.57e-5 * s**4 / (s**8 + 0.154*s**7 + 0.182*s**6 + 0.1710*s**5 + 1.07*s**4 + 0.790*s**3 + 0.249*s**2 + 0.0107*s + 0.027)

# Perform substitution
substitution = ((1 - z**-1) / (1 + z**-1))
substituted_expression = Ha_BP_s.subs(s, substitution)

# Simplify the expression
simplified_expression = sp.simplify(substituted_expression)

# Print the result
print("Expression in z:")
print(simplified_expression)


