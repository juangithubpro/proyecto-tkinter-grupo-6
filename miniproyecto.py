import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from basededato import *


#mostrar datos
# Función que se ejecuta al presionar el botón, abre una nueva ventana
def mostrar_base_datos():
    # Crear una nueva ventana
    ventana_datos = tk.Toplevel()
    ventana_datos.title("Contenido de la base de datos")
    
    # Crear un árbol (tabla) para mostrar los datos
    tree = ttk.Treeview(ventana_datos, columns=("ID", "Nombre", "Edad"), show='headings')
    tree.heading("ID", text="ID")
    tree.heading("Nombre", text="Nombre")
    tree.heading("Edad", text="Edad")
    
    # Conectar a la base de datos y realizar una consulta
    conn = sqlite3.connect('formulario.db')  # Cambia esto por el nombre de tu base de datos
    cursor = conn.cursor()
    
    # Supongamos que tienes una tabla llamada "personas" con las columnas id, nombre, edad
    cursor.execute("SELECT id, nombre FROM agenda")
    filas = cursor.fetchall()
    
    # Insertar los datos en el árbol
    for fila in filas:
        tree.insert("", tk.END, values=fila)
    
    tree.pack()
    
    # Cerrar la conexión
    conn.close()


#mensaje y guardar

def mostrarMensaje(titulo, mensaje):
    messagebox.showinfo(titulo, mensaje)

def guardar():
    crearTabla()
    if((nombre.get() == "") or (edad.get() == "")):
        mostrarMensaje("Error", "Debes completar todos los datos")
    else:
        datos = nombre.get(),genero.get(), email.get(),edad.get(),contrasena.get(),ciudad.get()
        mostrarMensaje("Guardar", "Contacto guardado")
        
       



# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Formulario Innovador")
ventana.geometry("300x300")
ventana.resizable(False, False)
ventana.configure(bg="#02111B")

# Definir la función que se ejecutará cuando se haga clic en el botón
def enviar_datos(event=None):  # Añadir 'event=None' para permitir que la función se llame desde el evento de tecla
    print("Nombre:", nombre.get())
    print("Edad:", edad.get())
    print("Email:", email.get())
    print("Contraseña:", contrasena.get())
    print("Género:", genero.get())
    print("Ciudad:", ciudad.get())

# Crear los widgets del formulario
tk.Label(ventana, text="Nombre:", bg="#02111B", fg="#FCFCFC", font="Terminal").grid(row=0, column=0)
nombre = tk.Entry(ventana)
nombre.grid(row=0, column=1, columnspan=3)

tk.Label(ventana, text="Edad:", bg="#02111B", fg="#FCFCFC", font="Terminal").grid(row=2, column=0)
edad = tk.Entry(ventana)
edad.grid(row=2, column=1)

tk.Label(ventana, text="Email:", bg="#02111B", fg="#FCFCFC", font="Terminal").grid(row=3, column=0)
email = tk.Entry(ventana)
email.grid(row=3, column=1)

tk.Label(ventana, text="Contraseña:", bg="#02111B", fg="#FCFCFC", font="Terminal").grid(row=4, column=0)
contrasena = tk.Entry(ventana, show="*")  # Para ocultar la contraseña
contrasena.grid(row=4, column=1)

tk.Label(ventana, text="Género:", bg="#02111B", fg="#FCFCFC", font="Terminal").grid(row=5, column=0)
genero = tk.StringVar()
genero.set("Masculino")
genero_optionmenu = tk.OptionMenu(ventana, genero, "Masculino", "Femenino")
genero_optionmenu.grid(row=5, column=1)

tk.Label(ventana, text="Ciudad:", bg="#02111B", fg="#FCFCFC", font="Terminal").grid(row=6, column=0)
ciudad = ttk.Combobox(ventana, state="readonly")  # Hacer que el Combobox sea de solo lectura

# Agregar "Ciudades" como la primera opción en la lista
ciudades = ["Ciudades", "Avia Terai", "Campo Largo", "Charata", "Colonia Benítez", "Colonia Elisa", "Colonias Unidas", 
            "Comandancia Frías", "Concepción del Bermejo", "Coronel Du Graty", "Corzuela", "El Paranacito", 
            "El Sauzalito", "Fontana", "Fortín Belgrano", "Gancedo", "General Pinedo", "Hermoso Campo", "Isla Soto", 
            "La Clotilde", "La Escondida", "La Leonesa", "La Tigra", "La Verde", "Las Breñas", "Las Garcitas", 
            "Las Hacheras", "Las Palmas", "Los Frentones", "Machagai", "Makallé", "Margarita Belén", 
            "Miraflores", "Misión Nueva Pompeya", "Napenay", "Pampa del Indio", "Pampa del Infierno", 
            "Presidencia de la Plaza", "Presidencia Roca", "Puerto Bermejo", "Puerto Las Palmas", 
            "Puerto Tirol", "Resistencia", "Quitilipi", "San Bernardo", "Paraje San Fernando", "San Martin", 
            "Santa Sylvina", "Taco Pozo", "Tres Isletas", "Villa Ángela", "Villa Berthet", "Villa Río Bermejito"]

ciudad['values'] = ciudades
ciudad.grid(row=6, column=1)
ciudad.current(0)  #  "Ciudades" como opción predeterminada

boton_enviar = ttk.Button(ventana,  text="Enviar", command=guardar)
boton_enviar.grid(row=7, column=1, columnspan=4)


#boton de ver usuarios

boton_usuarios = tk.Button(ventana, text="Usuarios", command=mostrar_base_datos)
boton_usuarios.grid(row=8, column=0)

# Asociar la tecla "Enter" con la función enviar_datos
ventana.bind('<Return>', enviar_datos)

ventana.mainloop()
