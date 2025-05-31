# Importamos los módulos necesarios:
# tkinter para la interfaz gráfica,
# filedialog para seleccionar archivos desde el explorador,
# y PIL para cargar y mostrar imágenes.
import tkinter as Tk
from tkinter import filedialog
from PIL import Image, ImageTk


#SR2

def import_img():
    ruta_imagen = filedialog.askopenfilename(
        title="Selecciona una imagen",
        filetypes=[("Archivos de imagen", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
    )
    if ruta_imagen:
        imagen = Image.open(ruta_imagen)        # Abrimos la imagen seleccionada
        imagen = imagen.resize((500, 400))      # Ajustamos su tamaño para que se vea bien
        imagen_tk = ImageTk.PhotoImage(imagen)  # Convertimos la imagen para usarla en Tkinter
        image_display_label.configure(image=imagen_tk)  # Mostramos la imagen en el label
        image_display_label.image = imagen_tk  # Guardamos la referencia para evitar errores

#SR2

#SR1

# Creamos la ventana principal
ventana = Tk.Tk()
ventana.title("Visor de Imagen")       
ventana.geometry("800x600")            
ventana.configure(bg="black")          

# Etiqueta de título en la parte superior
etiqueta = Tk.Label(
    ventana, text="Visor de imagen",
    font=("Arial", 16), fg="white", bg="black",
    padx=20, pady=20
)
etiqueta.pack(pady=10)

# Botón para subir imagen, ubicado en la parte inferior
boton = Tk.Button(
    ventana, text="Subir imagen",
    command=import_img, fg="white", bg="black",
    font="Arial", padx=20, pady=10
)
boton.pack(side=Tk.BOTTOM, pady=50)

#SR1

#SR2
# Etiqueta que servirá para mostrar la imagen cargada
image_display_label = Tk.Label(ventana, bg="black")
# Esta etiqueta ahora llenará el espacio entre la etiqueta superior y el botón inferior.
image_display_label.pack(pady=20, expand=True, fill=Tk.BOTH)
#SR2

# Inicia el bucle principal de la aplicación (mantiene la ventana abierta)
ventana.mainloop()