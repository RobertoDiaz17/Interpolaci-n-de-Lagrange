import numpy as np
import matplotlib.pyplot as plt

# Datos del problema
altitud = np.array([2.0, 4.0, 6.0, 8.0]) # en kilómetros
consumo = np.array([2500, 2300, 2150, 2050]) # en kg/h

# Función de interpolación de Lagrange
def lagrange_interpolation(x, x_points, y_points):
    n = len(x_points)
    result = 0
    for i in range(n):
        term = y_points[i]
        for j in range(n):
            if i != j:
                term *= (x - x_points[j]) / (x_points[i] - x_points[j])
        result += term
    return result

# a) Estima el consumo de combustible a una altitud de 5 km.
altitud_interp = 5.0
consumo_interp = lagrange_interpolation(altitud_interp, altitud, consumo)
print(f"El consumo de combustible estimado a una altitud de {altitud_interp} km es: {consumo_interp:.2f} kg/h")

# b) Dibuja la curva de interpolación con los datos originales.
altitud_grafica = np.linspace(min(altitud), max(altitud), 100)
consumo_grafica = [lagrange_interpolation(x, altitud, consumo) for x in altitud_grafica]

plt.figure(figsize=(8, 6))
plt.plot(altitud_grafica, consumo_grafica, label="Interpolación de Lagrange", color="blue")
plt.scatter(altitud, consumo, color="red", label="Datos medidos")
plt.scatter(altitud_interp, consumo_interp, color="green", marker='o', s=100, label=f"Estimación a altitud={altitud_interp} km")
plt.xlabel("Altitud (km)")
plt.ylabel("Consumo de Combustible (kg/h)")
plt.title("Predicción del Consumo de Combustible en Aeronaves mediante Interpolación de Lagrange")
plt.legend()
plt.grid(True)
plt.savefig("prediccion_consumo_aeronaves.png")
plt.show()