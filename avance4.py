import pygame
import sys
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from PIL import ImageTk, Image
import webbrowser

pygame.init()

def calcular_velocidad_final():
    initial_velocity = float(entry_velocidad_inicial.get())
    acceleration = float(entry_aceleracion.get())
    time = float(entry_tiempo.get())
    time_step = 0.1

    # Define colores
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Define la pantalla
    size = (1200, 200)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Movimiento Rectilíneo Uniforme Acelerado")

    # Define variables
    x = 0
    y = 0

    # Define reloj
    clock = pygame.time.Clock()

    # Listas para almacenar los datos de tiempo y velocidad
    tiempo_datos = []
    velocidad_datos = []

    # Bucle principal
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Actualiza la velocidad y la posición
        velocity = initial_velocity + acceleration * time
        displacement = initial_velocity * time + 0.5 * acceleration * time ** 2
        x = int(displacement)

        # Actualiza el tiempo
        time += time_step

        # Dibuja la pantalla
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLACK, [x, y, 50, 50])

        # Actualiza la pantalla
        pygame.display.flip()

        # Actualiza el resultado en la etiqueta
        mensaje_velocidad_final = "= La velocidad es de {:.2f} m/s".format(velocity)
        label_velocidad_final.configure(text=mensaje_velocidad_final)

        # Actualiza el ejemplo del movimiento rectilíneo uniforme
        ejemplo_texto = "Ejemplo: La posición es {} m".format(x)
        label_ejemplo.configure(text=ejemplo_texto)

        # Agrega los datos de tiempo y velocidad a las listas
        tiempo_datos.append(time)
        velocidad_datos.append(velocity)

        # Espera 60 milisegundos
        clock.tick(60)

        # Crea el gráfico de velocidad contra tiempo
        fig = Figure(figsize=(4, 3), dpi=100)
        fig.add_subplot(111).plot(tiempo_datos, velocidad_datos)
        canvas = FigureCanvas(fig)
        canvas.draw()

        # Convierte el gráfico a una imagen tkinter compatible
        image = ImageTk.PhotoImage(Image.frombytes('RGB', canvas.get_width_height(), canvas.tostring_rgb()))

        # Muestra la imagen en un label
        graph_label.configure(image=image)
        graph_label.image = image

        # Ejecuta el bucle principal de la ventana
        window.update()

def mostrar_formula():
    # Carga la imagen
    imagen_formula = Image.open("MURA.png")
    imagen_formula = imagen_formula.resize((400, 100), Image.ANTIALIAS)  # Ajusta el tamaño de la imagen

    # Convierte la imagen a un objeto PhotoImage de Tkinter
    imagen_tk = ImageTk.PhotoImage(imagen_formula)

    # Muestra la imagen en un label
    formula_label.configure(image=imagen_tk)
    formula_label.image = imagen_tk

def abrir_ejercicio():
    # Carga la imagen
    imagen_ejercicio = Image.open("t01.png")
    imagen_ejercicio = imagen_ejercicio.resize((400, 300), Image.ANTIALIAS)  # Ajusta el tamaño de la imagen

    # Convierte la imagen a un objeto PhotoImage de Tkinter
    imagen_tk = ImageTk.PhotoImage(imagen_ejercicio)

    # Muestra la imagen en un label
    ejercicio_label.configure(image=imagen_tk)
    ejercicio_label.image = imagen_tk

def abrir_informacion():
    # Abre la imagen de información
    webbrowser.open("T02.png")

def mostrar_imagen_t02():
    # Carga la imagen T02
    imagen_t02 = Image.open("T02.png")
    imagen_t02 = imagen_t02.resize((500, 400), Image.ANTIALIAS)  # Ajusta el tamaño de la imagen

    # Convierte la imagen a un objeto PhotoImage de Tkinter
    imagen_tk_t02 = ImageTk.PhotoImage(imagen_t02)

    # Muestra la imagen en el label imagen_label
    imagen_label.configure(image=imagen_tk_t02)
    imagen_label.image = imagen_tk_t02

def cerrar_ventana(event):
    if event.keysym == 'Escape':
        window.destroy()

window = tk.Tk()
window.title("Cálculo de Velocidad")
window.geometry("900x950+0+0")  # Posiciona la ventana en la esquina superior izquierda
window.configure(bg="#CCCCCC")

# Label para mostrar el gráfico
graph_label = tk.Label(window, bg="#CCCCCC")
graph_label.place(x=10, y=250)

# Etiqueta y campos de entrada para el cálculo de velocidad final
label_velocidad_inicial = tk.Label(window, text="Velocidad Inicial (m/s):", bg="#CCCCCC")
label_velocidad_inicial.place(x=10, y=10)
entry_velocidad_inicial = tk.Entry(window, text="", fg="black", font=("Arial", 9, "bold"))
entry_velocidad_inicial.place(x=180, y=10, width=75)

label_aceleracion = tk.Label(window, text="Aceleración (m/s²):", bg="#CCCCCC")
label_aceleracion.place(x=10, y=40)
entry_aceleracion = tk.Entry(window, text="", fg="black", font=("Arial", 9, "bold"))
entry_aceleracion.place(x=180, y=40, width=75)

label_tiempo = tk.Label(window, text="Tiempo (s):", bg="#CCCCCC")
label_tiempo.place(x=10, y=70)
entry_tiempo = tk.Entry(window, text="", fg="black", font=("Arial", 9, "bold"))
entry_tiempo.place(x=180, y=70, width=75)

button_calcular = tk.Button(window, text="Calcular", command=calcular_velocidad_final)
button_calcular.place(x=180, y=110)

label_velocidad_final = tk.Label(window, text="=", fg="dark blue", bg="#CCCCCC", font=("Arial", 9, "bold"))
label_velocidad_final.place(x=240, y=110)

# Label para mostrar el ejemplo del movimiento rectilíneo uniforme
label_ejemplo = tk.Label(window, text="", fg="black", bg="#CCCCCC")
label_ejemplo.place(x=100, y=140)

# Botón para mostrar la fórmula
button_formula = tk.Button(window, text="Fórmula", command=mostrar_formula)
button_formula.place(x=180, y=160)

# Label para mostrar la imagen de la fórmula
formula_label = tk.Label(window, bg="#CCCCCC")
formula_label.place(x=550, y=80)

# Botón para abrir el ejercicio
button_ejercicio = tk.Button(window, text="Ejercicio", command=abrir_ejercicio)
button_ejercicio.place(x=180, y=190)

# Label para mostrar la imagen del ejercicio
ejercicio_label = tk.Label(window, bg="#CCCCCC")
ejercicio_label.place(x=550, y=320)

# Botón para mostrar la imagen T02
button_t02 = tk.Button(window, text="Mostrar informacion", command=mostrar_imagen_t02)
button_t02.place(x=180, y=220)

# Label para mostrar la imagen T02
imagen_label = tk.Label(window, bg="#CCCCCC")
imagen_label.place(x=1000, y=200)

window.bind('<Escape>', cerrar_ventana)

# Ejecutar el bucle principal de la ventana
window.mainloop()
