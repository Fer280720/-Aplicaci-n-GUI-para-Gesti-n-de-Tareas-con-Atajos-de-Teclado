import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("400x450")
        self.root.resizable(False, False)

        # ======= Entrada de nueva tarea =======
        self.entry = tk.Entry(root, font=("Segoe UI", 12))
        self.entry.pack(pady=10, padx=10, fill=tk.X)
        self.entry.bind("<Return>", lambda event: self.add_task())

        # ======= Botones =======
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)

        self.add_btn = tk.Button(btn_frame, text="Añadir", width=12, command=self.add_task)
        self.add_btn.grid(row=0, column=0, padx=5)

        self.complete_btn = tk.Button(btn_frame, text="Completar", width=12, command=self.mark_completed)
        self.complete_btn.grid(row=0, column=1, padx=5)

        self.delete_btn = tk.Button(btn_frame, text="Eliminar", width=12, command=self.delete_task)
        self.delete_btn.grid(row=0, column=2, padx=5)

        # ======= Lista de tareas =======
        self.task_listbox = tk.Listbox(root, font=("Segoe UI", 12), height=15, selectmode=tk.SINGLE)
        self.task_listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # ======= Atajos de teclado =======
        self.root.bind("<c>", lambda event: self.mark_completed())   # Marcar como completada
        self.root.bind("<d>", lambda event: self.delete_task())      # Eliminar tarea
        self.root.bind("<Delete>", lambda event: self.delete_task()) # Eliminar con tecla Delete
        self.root.bind("<Escape>", lambda event: self.root.destroy())# Salir con Escape

    # ======= Función para añadir tareas =======
    def add_task(self):
        task = self.entry.get().strip()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Campo vacío", "Por favor escribe una tarea.")

    # ======= Función para marcar tareas como completadas =======
    def mark_completed(self):
        selection = self.task_listbox.curselection()
        if selection:
            index = selection[0]
            task = self.task_listbox.get(index)
            if task.startswith("[✓] "):
                # Desmarcar tarea completada
                task = task[4:]
            else:
                # Marcar tarea como completada
                task = "[✓] " + task
            self.task_listbox.delete(index)
            self.task_listbox.insert(index, task)
            self.task_listbox.select_set(index)
        else:
            messagebox.showinfo("Seleccionar tarea", "Selecciona una tarea para marcar como completada.")

    # ======= Función para eliminar tareas =======
    def delete_task(self):
        selection = self.task_listbox.curselection()
        if selection:
            self.task_listbox.delete(selection[0])
        else:
            messagebox.showinfo("Seleccionar tarea", "Selecciona una tarea para eliminar.")

# ======= Ejecutar aplicación =======
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
