import numpy as np
import matplotlib.pyplot as plt

# Datos del problema
profundidad = np.array([1.0, 2.5, 4.0, 5.5]) # en centímetros
temperatura = np.array([85, 78, 69, 60]) # en grados Celsius

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

# a) Estimar la temperatura a una profundidad de 3.0 cm
profundidad_interp = 3.0
temperatura_interp = lagrange_interpolation(profundidad_interp, profundidad, temperatura)
print(f"La temperatura estimada a una profundidad de {profundidad_interp} cm es: {temperatura_interp:.2f} °C")

# b) Representar gráficamente los datos junto con la interpolación en el rango [1.0, 5.5]
x_grafica = np.linspace(min(profundidad), max(profundidad), 100)
y_grafica = [lagrange_interpolation(x, profundidad, temperatura) for x in x_grafica]

plt.figure(figsize=(8, 6))
plt.plot(x_grafica, y_grafica, label="Interpolación de Lagrange", color="blue")
plt.scatter(profundidad, temperatura, color="red", label="Puntos de medición")
plt.scatter(profundidad_interp, temperatura_interp, color="green", marker='o', s=100, label=f"Interpolación en profundidad={profundidad_interp} cm")
plt.xlabel("Profundidad (cm)")
plt.ylabel("Temperatura (°C)")
plt.title("Estimación de la Temperatura en un Motor mediante Interpolación de Lagrange")
plt.legend()
plt.grid(True)
plt.savefig("estimacion_temperatura_motor.png")
plt.show()