import tkinter as tk
from tkinter import messagebox

# Clase Alumno que representa a cada estudiante
class Alumno:
    def __init__(self, dni, apellidos, nombre, nota):
        self.dni = dni  # DNI del alumno
        self.apellidos = apellidos  # Apellidos del alumno
        self.nombre = nombre  # Nombre del alumno
        self.nota = nota  # Nota numérica del alumno
        self.calificacion = self.calcular_calificacion()  # Calificación calculada automáticamente

    # Método para calcular la calificación en base a la nota
    def calcular_calificacion(self):
        if self.nota < 5:
            return "SS"  # Suspenso
        elif 5 <= self.nota < 7:
            return "AP"  # Aprobado
        elif 7 <= self.nota < 9:
            return "NT"  # Notable
        else:
            return "SB"  # Sobresaliente

# Clase para gestionar la interfaz y las operaciones
class GestionAlumnos:
    def __init__(self, root):
        self.alumnos = {}  # Diccionario para almacenar a los alumnos
        self.root = root  # Ventana principal de la aplicación
        self.root.title("Gestión de Calificaciones")  # Título de la ventana

        # Inicializa la interfaz de usuario
        self.init_ui()

    # Configura los elementos gráficos de la interfaz
    def init_ui(self):
        # Etiquetas y campos de entrada
        tk.Label(self.root, text="DNI:").grid(row=0, column=0)
        self.dni_entry = tk.Entry(self.root)
        self.dni_entry.grid(row=0, column=1)

        tk.Label(self.root, text="Apellidos:").grid(row=1, column=0)
        self.apellidos_entry = tk.Entry(self.root)
        self.apellidos_entry.grid(row=1, column=1)

        tk.Label(self.root, text="Nombre:").grid(row=2, column=0)
        self.nombre_entry = tk.Entry(self.root)
        self.nombre_entry.grid(row=2, column=1)

        tk.Label(self.root, text="Nota:").grid(row=3, column=0)
        self.nota_entry = tk.Entry(self.root)
        self.nota_entry.grid(row=3, column=1)

        # Botones para las diferentes funciones
        tk.Button(self.root, text="Introducir Alumno", command=self.introducir_alumno).grid(row=4, column=0)
        tk.Button(self.root, text="Eliminar Alumno", command=self.eliminar_alumno).grid(row=4, column=1)
        tk.Button(self.root, text="Consultar Nota", command=self.consultar_nota).grid(row=5, column=0)
        tk.Button(self.root, text="Modificar Nota", command=self.modificar_nota).grid(row=5, column=1)
        tk.Button(self.root, text="Mostrar Suspensos", command=self.mostrar_suspensos).grid(row=6, column=0)
        tk.Button(self.root, text="Mostrar Aprobados", command=self.mostrar_aprobados).grid(row=6, column=1)
        tk.Button(self.root, text="Mostrar Candidatos a MH", command=self.mostrar_candidatos_mh).grid(row=7, column=0)
        tk.Button(self.root, text="Mostrar Todos", command=self.mostrar_todos).grid(row=7, column=1)

    # Función para introducir un nuevo alumno
    def introducir_alumno(self):
        dni = self.dni_entry.get()  # Obtiene el DNI del campo de entrada
        apellidos = self.apellidos_entry.get()
        nombre = self.nombre_entry.get()
        try:
            nota = float(self.nota_entry.get())  # Convierte la nota a número
        except ValueError:
            messagebox.showerror("Error", "Nota debe ser un número.")  # Maneja errores de conversión
            return

        if dni in self.alumnos:
            messagebox.showerror("Error", "Ya existe un alumno con ese DNI.")  # Verifica duplicados
            return

        # Agrega el alumno al diccionario
        self.alumnos[dni] = Alumno(dni, apellidos, nombre, nota)
        messagebox.showinfo("Éxito", "Alumno introducido correctamente.")

    # Función para eliminar un alumno a partir del DNI
    def eliminar_alumno(self):
        dni = self.dni_entry.get()
        if dni in self.alumnos:
            del self.alumnos[dni]
            messagebox.showinfo("Éxito", "Alumno eliminado correctamente.")
        else:
            messagebox.showerror("Error", "No existe un alumno con ese DNI.")

    # Función para consultar la nota y calificación de un alumno
    def consultar_nota(self):
        dni = self.dni_entry.get()
        if dni in self.alumnos:
            alumno = self.alumnos[dni]
            messagebox.showinfo("Consulta", f"Nota: {alumno.nota}, Calificación: {alumno.calificacion}")
        else:
            messagebox.showerror("Error", "No existe un alumno con ese DNI.")

    # Función para modificar la nota de un alumno
    def modificar_nota(self):
        dni = self.dni_entry.get()
        try:
            nueva_nota = float(self.nota_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Nota debe ser un número.")
            return

        if dni in self.alumnos:
            self.alumnos[dni].nota = nueva_nota
            self.alumnos[dni].calificacion = self.alumnos[dni].calcular_calificacion()
            messagebox.showinfo("Éxito", "Nota modificada correctamente.")
        else:
            messagebox.showerror("Error", "No existe un alumno con ese DNI.")

    # Función para mostrar alumnos suspensos
    def mostrar_suspensos(self):
        suspensos = [f"{a.dni} {a.apellidos}, {a.nombre} {a.nota} {a.calificacion}"
                     for a in self.alumnos.values() if a.nota < 5]
        self.mostrar_lista("Alumnos Suspensos", suspensos)

    # Función para mostrar alumnos aprobados
    def mostrar_aprobados(self):
        aprobados = [f"{a.dni} {a.apellidos}, {a.nombre} {a.nota} {a.calificacion}"
                     for a in self.alumnos.values() if a.nota >= 5]
        self.mostrar_lista("Alumnos Aprobados", aprobados)

    # Función para mostrar alumnos candidatos a matrícula de honor
    def mostrar_candidatos_mh(self):
        mh = [f"{a.dni} {a.apellidos}, {a.nombre} {a.nota} {a.calificacion}"
              for a in self.alumnos.values() if a.nota == 10]
        self.mostrar_lista("Candidatos a MH", mh)

    # Función para mostrar todos los alumnos
    def mostrar_todos(self):
        todos = [f"{a.dni} {a.apellidos}, {a.nombre} {a.nota} {a.calificacion}"
                 for a in self.alumnos.values()]
        self.mostrar_lista("Todos los Alumnos", todos)

    # Función auxiliar para mostrar una lista en un cuadro de diálogo
    def mostrar_lista(self, titulo, lista):
        if lista:
            messagebox.showinfo(titulo, "\n".join(lista))
        else:
            messagebox.showinfo(titulo, "No hay datos que mostrar.")

# Código principal para ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()  # Crea la ventana principal
    app = GestionAlumnos(root)  # Instancia la clase de gestión
    root.mainloop()  # Inicia el bucle principal de la interfaz
