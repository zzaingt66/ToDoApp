def toDoApp()

    tareas = []
    def añadirTarea():
        state = True
        while state:
            tarea = input("Escriba la tarea que desea añadir: ")
            tareas.append(tarea)
            print(f"---- La tarea '{tarea}' fue guardada con éxito ----")
            no = input("¿Desea añadir otra tarea? (Enter para seguir, 'no' para salir): ")
            if no.lower() == 'no':
                state = False

    def verTarea():
        if len(tareas) != 0:
            print("\n", "_" * 20)
            print("Sus tareas pendientes son:")
            for i, tarea in enumerate(tareas, start=1):
                print(f"Tarea {i} : {tarea}")
                print("\n", "_" * 20)
        else:
            print("Usted no tiene tareas pendientes")

    def eliminarTarea():
        verTarea()
        rm = int(input("Qué tarea desea eliminar? "))
        if rm > 0 and rm <= len(tareas):
            deleteTask = tareas.pop(rm - 1)
            print(f"La tarea '{deleteTask}' fue eliminada correctamente!")
        else:
            print("Número de tarea inválido.")

    def modificarTarea():
        verTarea()
        taskIndex = int(input("Qué tarea desea eliminar?\n "))
        taskModify = input("Ingrese la actualización de su tarea: ")
        if len(tareas) < taskIndex < len(tareas):
            print("La tarea no existe")
        else:
            tareas[taskIndex - 1] = taskModify

    def mostrarMenu():
        print("\nBienvenido a este ToDo App")
        print("Qué desea hacer?")
        print(" 1. Agregar tarea")
        print(" 2. Ver tareas")
        print(" 3. Eliminar tarea")
        print(" 4. Modificar tarea")
        print(" 5. Salir")

    def menu():
        opciones = {
            "1": añadirTarea,
            "2": verTarea,
            "3": eliminarTarea,
            "4": modificarTarea
        }
        state = True
        while state:
            mostrarMenu()
            opcion = input("  ")
            if opcion in opciones:
                opciones[opcion]()
            elif opcion == "5":
                print("Chaop")
                state = False
            else:
                print("No existe esta opción")

    menu()

toDoApp()
