import re

# Paso los controladores


class BlogController:
    def __init__(self, model):
        self.model = model

    def validar(self, title, email):
        # Valido formato de titulo y mail, uso regex para verificacion
        title_pattern = "^[A-Za-z]+(?:[ _-][A-Za-z]+)*$"
        if not re.match(title_pattern, title):
            return "Título no válido."

        # Valido formato de mail
        email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not re.match(email_pattern, email):
            return "Por favor, introduce un email válido."

        return True

    def control_alta(self, title, content, email, tree, message_label):
        # Agrego  excepciones
        try:
            # Pregunto por validacion
            validation_result = self.validar(title, email)
            if validation_result == True:
                # Doy alta
                self.model.alta(title, content, email)
                # actualizo treeview
                self.actualizar_treeview(tree, message_label)
            else:
                message_label.config(text=validation_result)
        except Exception as e:
            message_label.config(text=f"Error: {str(e)}")

    def control_modificar(self, id, title, content, email, tree, message_label):
        # Agrego  excepciones
        try:
            # pregunto por validacion
            validation_result = self.validar(title, email)
            if validation_result == True:
                # Hago modificar
                self.model.modificar(id, title, content, email)
                # actualizo treeview
                self.actualizar_treeview(tree, message_label)
            else:
                message_label.config(text=validation_result)
        except Exception as e:
            message_label.config(text=f"Error: {str(e)}")

    def borrar(self, tree, message_label):
        # seleciono valor a borrar
        selected = tree.selection()
        # Agrego condicional para verificar seleccion
        if selected:
            item = tree.item(selected)
            mi_id = item["text"]
            # defino instrucciones
            self.model.borrar(mi_id)
            tree.delete(selected)
            message_label.config(text="Entrada borrada con éxito.")
        else:
            message_label.config(text="Error: No se seleccionó ninguna entrada.")

    # Funcion consultar
    def consultar(self, tree, a_val, b_val, c_val):
        # Seleciono
        selected = tree.selection()
        # Si resultado existe
        if selected:
            item = tree.item(selected)
            # Lo posisiono en las tres entradas
            a_val.set(item["values"][0])
            b_val.set(item["values"][1])
            c_val.set(item["values"][2])
            return item["text"]
        else:
            message_label.config(text="Error: No se seleccionó ninguna entrada.")

    # actualizar tree
    def actualizar_treeview(self, tree, message_label):
        records = tree.get_children()
        for element in records:
            tree.delete(element)
        resultado = self.model.consultar()
        for fila in resultado:
            tree.insert(
                "", 0, text=fila[0], values=(fila[1], fila[2], fila[3], fila[4])
            )
        message_label.config(text="Base de datos actualizada con éxito.")
