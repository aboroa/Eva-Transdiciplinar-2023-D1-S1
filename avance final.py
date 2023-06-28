 # Matias Gutierrez, Jorge Fernandez, Alfonzo Boroa

import pygame                                                        # Importa la biblioteca pygame para el desarrollo de juegos
import sys                                                           # Importa el módulo sys para operaciones relacionadas con el sistema
import tkinter as tk                                                 # Importa la biblioteca tkinter para GUI
import matplotlib.pyplot as plt                                     # Importa la biblioteca matplotlib para trazar gráficos
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas  # Importa FigureCanvas de matplotlib para renderizar figuras en tkinter
from matplotlib.figure import Figure                                # Importa Figure de matplotlib para crear figuras
from PIL import ImageTk, Image                                       # Importa ImageTk e Image de PIL para operaciones con imágenes
pygame.init()                                                   # Inicializa la biblioteca pygame


def calcular_velocidad_final():                                      # Define una función para calcular la velocidad final
    initial_velocity = float(entry_velocidad_inicial.get())          # Obtiene la velocidad inicial del campo de entrada y la convierte en un número decimal
    acceleration = float(entry_aceleracion.get())                    # Obtiene la aceleración del campo de entrada y la convierte en un número decimal
    time = float(entry_tiempo.get())                                 # Obtiene el tiempo del campo de entrada y lo convierte en un número decimal
    time_step = 0.1                                                  # Define el paso de tiempo

    NEGRO = (0, 0, 0)                                                # Define el color negro
    BLANCO = (255, 255, 255)                                          # Define el color blanco

    tamaño = (1200, 200)                                              # Define el tamaño de la ventana del juego
    pantalla = pygame.display.set_mode(tamaño)                        # Crea la ventana del juego con el tamaño especificado
    pygame.display.set_caption("Movimiento Rectilíneo Uniforme Acelerado")  # Establece el título de la ventana del juego

    x = 0                                                             # Inicializa la coordenada x
    y = 0                                                             # Inicializa la coordenada y

    reloj = pygame.time.Clock()                                       # Crea un objeto de reloj para controlar la velocidad de fotogramas

    tiempo_datos = []                                                 # Crea listas vacías para almacenar los datos de tiempo y velocidad
    velocidad_datos = []

    while True:                                                       # Inicia el bucle principal del juego
        for event in pygame.event.get():                              # Verifica los eventos
            if event.type == pygame.QUIT:                             # Si el usuario cierra la ventana, sale del programa
                sys.exit()

        # Actualiza la velocidad y la posición
        velocidad = initial_velocity + acceleration * time              # Calcula la velocidad utilizando la fórmula proporcionada
        desplazamiento = initial_velocity * time + 0.5 * acceleration * time ** 2  # Calcula el desplazamiento utilizando la fórmula proporcionada
        x = int(desplazamiento)                                        # Convierte el desplazamiento a un entero para dibujar

        # Actualiza el tiempo
        time += time_step                                              # Incrementa el tiempo

        # Dibuja la pantalla
        pantalla.fill(BLANCO)                                          # Rellena la pantalla con color blanco
        pygame.draw.rect(pantalla, NEGRO, [x, y, 50, 50])        # # Dibuja un rectángulo que representa la posición del objeto

        # Actualiza la pantalla
        pygame.display.flip()                                 # # Actualiza la pantalla


        # Actualiza el resultado en la etiqueta
        mensaje_velocidad_final = "= La velocidad es de {:.2f} m/s".format(velocidad)  # Crea un mensaje con la velocidad calculada
        label_velocidad_final.configure(text=mensaje_velocidad_final)  # Actualiza la etiqueta con el mensaje de velocidad

        # Actualiza el ejemplo del movimiento rectilíneo uniforme
        ejemplo_texto = "Ejemplo: La posición es {} m".format(x)       # Crea un mensaje con la posición actual
        label_ejemplo.configure(text=ejemplo_texto)                    # Actualiza la etiqueta con el mensaje de posición

        # Agrega los datos de tiempo y velocidad a las listas
        tiempo_datos.append(time)                               # # Agrega el tiempo actual y la velocidad a las listas respectivas
        velocidad_datos.append(velocidad)

        # Espera 60 milisegundos
        reloj.tick(60)                          # Limita la velocidad de fotogramas a 60 FPS

        fig = Figure(figsize=(4, 3), dpi=100)                          # Crea una figura para el gráfico de velocidad vs. tiempo
        fig.add_subplot(111).plot(tiempo_datos, velocidad_datos)       # Agrega un subgráfico a la figura y traza los datos
        canvas = FigureCanvas(fig)                                     # Crea un objeto FigureCanvas con la figura
        canvas.draw()                                                  # Dibuja la figura en el lienzo

        imagen = ImageTk.PhotoImage(Image.frombytes('RGB', canvas.get_width_height(), canvas.tostring_rgb()))  # Convierte la figura en una imagen compatible con tkinter

        graph_label.configure(image=imagen)                            # Actualiza la etiqueta con la imagen del gráfico
        graph_label.image = imagen

        # Ejecuta el bucle principal de la ventana
        window.update()

def mostrar_formula():                                                # Define una función para mostrar la fórmula
    imagen_formula = Image.open("MURA.png")                           # Abre la imagen de la fórmula
    imagen_formula = imagen_formula.resize((400, 100), Image.ANTIALIAS)  # Cambia el tamaño de la imagen
    imagen_tk = ImageTk.PhotoImage(imagen_formula)                     # Convierte la imagen en un objeto compatible con tkinter
    formula_label.configure(image=imagen_tk)                          # Actualiza la etiqueta con la imagen de la fórmula
    formula_label.image = imagen_tk

def abrir_ejercicio():                                                # Define una función para abrir una imagen de ejercicio
    imagen_ejercicio = Image.open("t01.png")                          # Abre la imagen de ejercicio
    imagen_ejercicio = imagen_ejercicio.resize((400, 300), Image.ANTIALIAS)  # Cambia el tamaño de la imagen
    imagen_tk = ImageTk.PhotoImage(imagen_ejercicio)                   # Convierte la imagen en un objeto compatible con tkinter
    ejercicio_label.configure(image=imagen_tk)                        # Actualiza la etiqueta con la imagen de ejercicio
    ejercicio_label.image = imagen_tk

def abrir_informacion():                                              # Define una función para abrir una imagen de información
    webbrowser.open("T02.png")                                        # Abre la imagen de información en el navegador web predeterminado

def mostrar_imagen_t02():                                             # Define una función para mostrar la imagen T02
    imagen_t02 = Image.open("T02.png")                                # Abre la imagen T02
    imagen_t02 = imagen_t02.resize((500, 400), Image.ANTIALIAS)       # Cambia el tamaño de la imagen
    imagen_tk_t02 = ImageTk.PhotoImage(imagen_t02)                     # Convierte la imagen en un objeto compatible con tkinter
    imagen_label.configure(image=imagen_tk_t02)                       # Actualiza la etiqueta con la imagen T02
    imagen_label.image = imagen_tk_t02

def cerrar_ventana(event):                                            # Define una función para cerrar la ventana cuando se presiona la tecla Escape
    if event.keysym == 'Escape':
        window.destroy()

window = tk.Tk()                                                      # Crea la ventana de tkinter
window.title("Cálculo de Velocidad")                                  # Establece el título de la ventana
window.geometry("900x950+0+0")                                       # Establece el tamaño y la posición de la ventana
window.configure(bg="#CCCCCC")                                        # Establece el color de fondo de la ventana


# Label para mostrar el gráfico
graph_label = tk.Label(window, bg="#CCCCCC")                          # Crea una etiqueta para mostrar el gráfico
graph_label.place(x=10, y=250)                                        # Establece la posición de la etiqueta


# Etiqueta y campos de entrada para el cálculo de velocidad final
label_velocidad_inicial = tk.Label(window, text="Velocidad Inicial (m/s):", bg="#CCCCCC")  # Crea una etiqueta para la velocidad inicial
label_velocidad_inicial.place(x=10, y=10)                             # Establece la posición de la etiqueta
entry_velocidad_inicial = tk.Entry(window, text="", fg="black", font=("Arial", 9, "bold"))  # Crea un campo de entrada para la velocidad inicial
entry_velocidad_inicial.place(x=180, y=10, width=75)                  # Establece la posición y el tamaño del campo de entrada

label_aceleracion = tk.Label(window, text="Aceleración (m/s²):", bg="#CCCCCC")  # Crea una etiqueta para la aceleración
label_aceleracion.place(x=10, y=40)                                   # Establece la posición de la etiqueta
entry_aceleracion = tk.Entry(window, text="", fg="black", font=("Arial", 9, "bold"))  # Crea un campo de entrada para la aceleración
entry_aceleracion.place(x=180, y=40, width=75)                        # Establece la posición y el tamaño del campo de entrada


label_tiempo = tk.Label(window, text="Tiempo (s):", bg="#CCCCCC")     # Crea una etiqueta para el tiempo
label_tiempo.place(x=10, y=70)                                        # Establece la posición de la etiqueta
entry_tiempo = tk.Entry(window, text="", fg="black", font=("Arial", 9, "bold"))  # Crea un campo de entrada para el tiempo
entry_tiempo.place(x=180, y=70, width=75)                             # Establece la posición y el tamaño del campo de entrada

button_calcular = tk.Button(window, text="Calcular", command=calcular_velocidad_final)  # Crea un botón para calcular la velocidad final
button_calcular.place(x=180, y=110)                                   # Establece la posición del botón


label_velocidad_final = tk.Label(window, text="=", fg="dark blue", bg="#CCCCCC", font=("Arial", 9, "bold"))  # Crea una etiqueta para mostrar la velocidad final
label_velocidad_final.place(x=240, y=110)                             # Establece la posición de la etiqueta

# Label para mostrar el ejemplo del movimiento rectilíneo uniforme
label_ejemplo = tk.Label(window, text="", fg="black", bg="#CCCCCC")   # Crea una etiqueta para mostrar el ejemplo de movimiento lineal uniforme
label_ejemplo.place(x=100, y=140)                                     # Establece la posición de la etiqueta
# Botón para mostrar la fórmula
button_formula = tk.Button(window, text="Fórmula", command=mostrar_formula) # crea boton
button_formula.place(x=180, y=160)                                          # posiciona boton

# Label para mostrar la imagen de la fórmula
formula_label = tk.Label(window, bg="#CCCCCC")
formula_label.place(x=550, y=80)

# Botón para abrir el ejercicio
button_ejercicio = tk.Button(window, text="Ejercicio", command=abrir_ejercicio) # crea boton
button_ejercicio.place(x=180, y=190)                                            # posiciona boton

# Label para mostrar la imagen del ejercicio
ejercicio_label = tk.Label(window, bg="#CCCCCC")
ejercicio_label.place(x=550, y=320)

# Botón para mostrar la imagen T02
button_t02 = tk.Button(window, text="Mostrar informacion", command=mostrar_imagen_t02)  # crea bton
button_t02.place(x=180, y=220)                                                          # posiciona boton

# Label para mostrar la imagen T02
imagen_label = tk.Label(window, bg="#CCCCCC")
imagen_label.place(x=1000, y=200)

window.bind('<Escape>', cerrar_ventana)             # Vincula la función cerrar_ventana al evento de presionar una tecla

# Ejecutar el bucle principal de la ventana
window.mainloop()                         #  # Ejecuta el bucle principal de tkinter
