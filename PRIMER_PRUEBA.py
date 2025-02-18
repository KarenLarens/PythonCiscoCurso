import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title("Tabla en Tkinter")

# Crear el Treeview
columns = ("ID", "Nombre", "Edad")
tree = ttk.Treeview(root, columns=columns, show="headings")

# Definir encabezados
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)  # Ajustar el ancho de las columnas

# Agregar datos a la tabla
datos = [
    (1, "Ana", 25),
    (2, "Luis", 30),
    (3, "Sofía", 28),
]

for dato in datos:
    tree.insert("", tk.END, values=dato)

# Empaquetar y mostrar la tabla
tree.pack(expand=True, fill="both")

# Iniciar la aplicación
root.mainloop()
