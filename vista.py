from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk
from modelo import BlogModel
from controlador import BlogController


# Creacion de clase para vista
class Vista:
    # Defino el constructor de atributos
    def __init__(self, window):
        # Digo que self.root es igual a window, el parametro con el que paso ventana al final
        self.root = window
        # Despues los transformo en atributos de instancia para ser invocados
        self.root.title("Blog App")
        self.root.config(bg="floral white")
        self.root.geometry("1024x768")

        # Creo un objeto para usar los metodos del modelo
        self.objeto_blogmodel = BlogModel()
        # Creo un objeto con los metodos controlador, le paso el modelo
        self.objeto_blogcontroller = BlogController(self.objeto_blogmodel)

        self.titulo = Label(
            self.root,
            text="Crea Contenido Informativo",
            bg="gray10",
            fg="thistle1",
            height=1,
            width=60,
        )
        self.titulo.grid(row=0, column=1, columnspan=4, padx=1, sticky=W + E)

        self.titulo_blog = Label(self.root, text="Titulo del Blog")
        self.titulo_blog.grid(row=1, column=1, sticky=W + E)
        self.cont_blog = Label(self.root, text="Contenido del Blog")
        self.cont_blog.grid(row=2, column=1, sticky=W + E)
        self.email_blog = Label(self.root, text="Email")
        self.email_blog.grid(row=3, column=1, sticky=W + E)

        # Defino variables para tomar valores de campos de entrada
        self.a_val, self.b_val, self.c_val = StringVar(), StringVar(), StringVar()
        self.w_ancho = 20

        self.entrada1 = Entry(self.root, textvariable=self.a_val, width=100)
        self.entrada1.grid(row=1, column=2)
        self.entrada2 = Entry(self.root, textvariable=self.b_val, width=100)
        self.entrada2.grid(row=2, column=2)
        self.entrada3 = Entry(self.root, textvariable=self.c_val, width=100)
        self.entrada3.grid(row=3, column=2)

        # Treeview

        self.tree = ttk.Treeview(self.root)
        self.tree["columns"] = ("col1", "col2", "col3", "col4")
        self.tree.column("#0", width=50, minwidth=50, anchor=W)
        self.tree.column("col1", width=200, minwidth=150, anchor=W)
        self.tree.column("col2", width=500, minwidth=150, anchor=W)
        self.tree.column("col3", width=150, minwidth=120, anchor=W)
        self.tree.column("col4", width=120, minwidth=120, anchor=W)

        self.tree.heading("#0", text="ID")
        self.tree.heading("col1", text="Titulo del Blog")
        self.tree.heading("col2", text="Contenido")
        self.tree.heading("col3", text="Email")
        self.tree.heading("col4", text="Fecha")
        self.tree.grid(row=9, column=1, columnspan=4)

        # Mensajes

        self.message_label = Label(self.root, text="", fg="red", bg="floral white")
        self.message_label.grid(row=8, column=1, columnspan=2)

        # Botones

        self.boton_alta = Button(
            self.root,
            text="Alta",
            command=lambda: self.objeto_blogcontroller.control_alta(
                self.a_val.get(),
                self.b_val.get(),
                self.c_val.get(),
                self.tree,
                self.message_label,
            ),
        )
        self.boton_alta.grid(row=4, column=2)

        self.boton_consulta = Button(
            self.root,
            text="Consultar",
            command=lambda: self.objeto_blogcontroller.consultar(
                self.tree, self.a_val, self.b_val, self.c_val
            ),
        )
        self.boton_consulta.grid(row=5, column=2)

        self.boton_modificar = Button(
            self.root,
            text="Modificar",
            command=lambda: self.objeto_blogcontroller.control_modificar(
                self.tree.item(self.tree.selection())["text"],
                self.a_val.get(),
                self.b_val.get(),
                self.c_val.get(),
                self.tree,
                self.message_label,
            ),
        )
        self.boton_modificar.grid(row=6, column=2)

        self.boton_borrar = Button(
            self.root,
            text="Borrar",
            command=lambda: self.objeto_blogcontroller.borrar(
                self.tree, self.message_label
            ),
        )
        self.boton_borrar.grid(row=7, column=2)
