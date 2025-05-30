#importar tkinter
import tkinter as Tk

#SR1

#definir funcion para usar posteriormente(actualmente cierra la ventana)
def import_img():
    ventana.destroy() 
#crea la ventana principal de la app
ventana = Tk.Tk()
#Establece el titulo
ventana.title("Visor")
#Establece el tamaño
ventana.geometry("800x600")
#Establece el color de fondo
ventana.configure(bg="black")


#Crea la etiqueta que se utiliza como titulo
etiqueta = Tk.Label(ventana, text="Visor de imagen", font=("Arial", 16))
etiqueta.configure(fg="white", bg="black", padx=20, pady=20)
etiqueta.pack(pady=10)
#Crea el boton que se encarga de subir la imagen
boton= Tk.Button(ventana, text="Subir imagen")
boton.configure(fg="white", bg="black", font="Arial", padx=20, pady=10, command= import_img)
boton.pack(side=Tk.BOTTOM, pady= 50)
#Despliega la ventana
ventana.mainloop()

#SR1