
import pygame
import sys
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from PIL import ImageTk, Image

pygame.init()

def calcular_velocidad_final():
    initial_velocity = float(entry_velocidad_inicial.get())
    acceleration = float(entry_aceleracion.get())
    time = float(entry_tiempo.get())
    time_step = 0.1

    # Definir colores
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Definir la pantalla
    size = (1200, 200)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Movimiento Rectilíneo Uniforme Acelerado")

    # Definir variables
    x = 0
    y = 0

    # Definir reloj
    clock = pygame.time.Clock()

    # Listas para almacenar los datos de tiempo y velocidad
    tiempo_datos = []
    velocidad_datos = []

    # Bucle principal
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Actualizar la velocidad y la posición
        velocity = initial_velocity + acceleration * time
        displacement = initial_velocity * time + 0.5 * acceleration * time ** 2
        x = int(displacement)

        # Actualizar el tiempo
        time += time_step

        # Dibujar la pantalla
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLACK, [x, y, 50, 50])

        # Actualizar la pantalla
        pygame.display.flip()

        # Actualizar el resultado en la etiqueta
        mensaje_velocidad_final = "= La velocidad es de {:.2f} m/s".format(velocity)
        label_velocidad_final.configure(text=mensaje_velocidad_final)

        # Agregar los datos de tiempo y velocidad a las listas
        tiempo_datos.append(time)
        velocidad_datos.append(velocity)

        # Esperar 60 milisegundos
        clock.tick(60)

        # Crear el gráfico de velocidad contra tiempo
        fig = Figure(figsize=(4, 3), dpi=100)
        fig.add_subplot(111).plot(tiempo_datos, velocidad_datos)
        canvas = FigureCanvas(fig)
        canvas.draw()

        # Convertir el gráfico a una imagen tkinter compatible
        image = ImageTk.PhotoImage(Image.frombytes('RGB', canvas.get_width_height(), canvas.tostring_rgb()))

        # Mostrar la imagen en un label
        graph_label.configure(image=image)
        graph_label.image = image

        # Ejecutar el bucle principal de la ventana
        window.update()

def cerrar_ventana(event):
    if event.keysym == 'Escape':
        window.destroy()

window = tk.Tk()
window.title("Cálculo de Velocidad")
window.geometry("700x400")
window.configure(bg="#CCCCCC")

# Etiquetas y campos de entrada para el cálculo de velocidad final
label_velocidad_inicial = tk.Label(window, text="Velocidad Inicial (m/s):", bg="#CCCCCC")
label_velocidad_inicial.place(x=10, y=20)
entry_velocidad_inicial = tk.Entry(window, text="", fg="black", font=("Arial", 9, "bold"))
entry_velocidad_inicial.place(x=180, y=20, width=75)

label_aceleracion = tk.Label(window, text="Aceleración (m/s²):", bg="#CCCCCC")
label_aceleracion.place(x=10, y=50)
entry_aceleracion = tk.Entry(window, text="", fg="black", font=("Arial", 9, "bold"))
entry_aceleracion.place(x=180, y=50, width=75)

label_tiempo = tk.Label(window, text="Tiempo (s):", bg="#CCCCCC")
label_tiempo.place(x=10, y=80)
entry_tiempo = tk.Entry(window, text="", fg="black", font=("Arial", 9, "bold"))
entry_tiempo.place(x=180, y=80, width=75)

button_calcular = tk.Button(window, text="Calcular", command=calcular_velocidad_final)
button_calcular.place(x=180, y=120)

label_velocidad_final = tk.Label(window, text="=", fg="dark blue", bg="#CCCCCC", font=("Arial", 9, "bold"))
label_velocidad_final.place(x=240, y=120)

# Label para mostrar el gráfico
graph_label = tk.Label(window, bg="#CCCCCC")
graph_label.place(x=350, y=20)

window.bind('<Escape>', cerrar_ventana)

# Ejecutar el bucle principal de la ventana
window.mainloop()
