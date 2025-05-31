# Importamos los módulos necesarios:
# tkinter para la interfaz gráfica,
# filedialog para seleccionar archivos desde el explorador,
# y PIL para cargar y mostrar imágenes.
import tkinter as Tk
from tkinter import filedialog
from PIL import Image, ImageTk


# Variables globales para gestionar la imagen actual y su rotación
current_pil_image = None 
current_angle = 0        

#SR2

#Funcion para importar la imagen
def import_img():
    global current_pil_image, current_angle 
    ruta_imagen = filedialog.askopenfilename(
        title="Selecciona una imagen",
        filetypes=[("Archivos de imagen", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
    )
    if ruta_imagen:
        imagen_cargada = Image.open(ruta_imagen)        # Abrimos la imagen seleccionada
        imagen_redimensionada = imagen_cargada.resize((500, 400), Image.Resampling.LANCZOS) # Ajustamos su tamaño
        
        current_pil_image = imagen_redimensionada  
       
        # Reiniciamos el ángulo a 0 para la nueva imagen
        current_angle = 0                         
        
        imagen_tk = ImageTk.PhotoImage(current_pil_image)  # Convertimos la imagen para usarla en Tkinter
        image_display_label.configure(image=imagen_tk) 
        image_display_label.image = imagen_tk  

#SR2

#SR3

#Funcion para rotar la imagen
def rotar_imagen_accion():
    global current_pil_image, current_angle

    if current_pil_image: 
        current_angle = (current_angle + 30) % 360 
        
        # Rotamos la imagen PIL original
        imagen_rotada_pil = current_pil_image.rotate(current_angle, expand=True, resample=Image.Resampling.BICUBIC)
        
        imagen_rotada_tk = ImageTk.PhotoImage(imagen_rotada_pil)
        image_display_label.configure(image=imagen_rotada_tk)
        image_display_label.image = imagen_rotada_tk 
    else:
        print("Carga una imagen primero.")

#SR3

#SR1

# Creamos la ventana principal
ventana = Tk.Tk()
ventana.title("Visor de Imagen")       
ventana.geometry("1200x800")            
ventana.configure(bg="black")          

# Configurar el layout de la ventana con grid
ventana.rowconfigure(0, weight=0)  
ventana.rowconfigure(1, weight=1)  
ventana.rowconfigure(2, weight=0)  
ventana.columnconfigure(0, weight=1) 

# Etiqueta de título
etiqueta = Tk.Label(
    ventana, text="Visor de imagen",
    font=("Arial", 16), fg="white", bg="black",
    padx=20, pady=20)
etiqueta.grid(row=0, column=0, sticky="ew", pady=10)
#SR1

#SR2

# Etiqueta que servirá para mostrar la imagen cargada
image_display_label = Tk.Label(ventana, bg="black")
image_display_label.grid(row=1, column=0, sticky="nsew", pady=20) 

#SR2

#SR1

# Crear un Frame para contener los botones y colocarlos en la parte inferior
button_frame = Tk.Frame(ventana, bg="black") 
button_frame.grid(row=2, column=0, sticky="ew", pady=(10, 20)) 

# Botón para subir imagen
boton_importar = Tk.Button(
    button_frame, text="Subir imagen",
    command=import_img, fg="white", bg="black",
    font=("Arial", 12), padx=20, pady=10 )
boton_importar.pack(side=Tk.LEFT, padx=(0, 5)) 

# Botón para rotar la imagen
boton_rotar = Tk.Button(
    button_frame, text="Rotar 30°",
    command=rotar_imagen_accion, fg="white", bg="black",
    font=("Arial", 12), padx=10, pady=10)
boton_rotar.pack(side=Tk.LEFT, padx=(5, 0)) 

# Inicia el bucle principal de la aplicación
ventana.mainloop()

#SR1