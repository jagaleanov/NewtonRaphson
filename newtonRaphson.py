from sympy import symbols, Matrix, Eq, solve

# Re-defining necessary components due to environment reset
x, y = symbols('x y')

# Coordenadas y distancias conocidas
xA, yA = 0, 0
xB, yB = 4, 0
xC, yC = 2, 3
dA, dB, dC = 5, 3, 2

# Funciones y derivadas
def f1(x, y):
    return (x - xA)**2 + (y - yA)**2 - dA**2

def f2(x, y):
    return (x - xB)**2 + (y - yB)**2 - dB**2

def f3(x, y):
    return (x - xC)**2 + (y - yC)**2 - dC**2

def J(x, y):
    return Matrix([
        [2*(x - xA), 2*(y - yA)],
        [2*(x - xB), 2*(y - yB)],
        [2*(x - xC), 2*(y - yC)]
    ])

def F(x, y):
    return Matrix([f1(x, y), f2(x, y), f3(x, y)])

# Inicializar variables
x_n, y_n = 3, 1  # Punto inicial

# Iteraciones del método de Newton-Raphson
iterations = 5  # Número de iteraciones
results = [(x_n, y_n)]

for i in range(iterations):
    try:
        # Calcula la inversa del promedio de las derivadas parciales 
        J_inv = J(x_n, y_n).pinv()
        # Actualiza x_n, y_n
        x_n, y_n = Matrix([x_n, y_n]) - J_inv * F(x_n, y_n)
        # Evalúa las nuevas posiciones
        x_n, y_n = x_n.evalf(), y_n.evalf()
        results.append((x_n, y_n))
        # Imprime los resultados de la iteración
        print(f"Iteration {i + 1}: x = {x_n}, y = {y_n}")
    except Exception as e:
        print(f"An error occurred: {e}")
        break

results
