#!/usr/bin/env python3
"""Herramienta de terminal ligera para gestionar una lista de tareas (todos).

Funcionalidades base:
- Agregar una nueva tarea por titulo
- Mostrar todas las tareas pendientes con su posicion numerica
- Eliminar una tarea por su posicion en la lista

No se soporta edicion de tareas: para modificar una tarea, se debe
eliminar y volver a crear.
"""


def add_one_task(title_or_tareas, tareas_or_title=None):
    """Agrega una nueva tarea por titulo a una lista en memoria.

    Acepta tanto add_one_task(title, tareas) como add_one_task(tareas, title).
    """
    if isinstance(title_or_tareas, list):
        tareas = title_or_tareas
        titulo = tareas_or_title
    elif isinstance(tareas_or_title, list):
        titulo = title_or_tareas
        tareas = tareas_or_title
    else:
        titulo = title_or_tareas
        tareas = tareas_or_title

    if tareas is None:
        raise ValueError("Se debe especificar una lista donde agregar la tarea.")

    titulo = str(titulo).strip() if titulo is not None else ""
    if not titulo:
        raise ValueError("El titulo de la tarea no puede estar vacio.")
    tareas.append(titulo)
    return tareas


def agregar_tarea(tareas, titulo):
    """Agrega una nueva tarea por titulo a la lista (en memoria)."""
    return add_one_task(tareas, titulo)


def delete_task(number_to_delete, tareas=None):
    """Elimina una tarea de la lista en memoria usando su posicion (1-indexada).

    Acepta tanto delete_task(number_to_delete, tareas) como
    delete_task(tareas, number_to_delete). Devuelve el titulo eliminado.
    """
    if isinstance(number_to_delete, list):
        tareas, number_to_delete = number_to_delete, tareas

    if tareas is None:
        raise ValueError("Se debe especificar una lista de la cual eliminar la tarea.")

    posicion = int(number_to_delete)
    if posicion < 1 or posicion > len(tareas):
        raise IndexError("Posicion fuera de rango.")
    return tareas.pop(posicion - 1)


def eliminar_tarea(tareas, posicion):
    """Elimina una tarea por su posicion (1-indexada). Devuelve el titulo eliminado."""
    return delete_task(tareas, posicion)


def print_list(tareas):
    """Muestra todas las tareas pendientes con su posicion numerica."""
    if not tareas:
        print("No hay tareas pendientes.")
        return
    for i, titulo in enumerate(tareas, start=1):
        print(f"{i}. {titulo}")


def mostrar_tareas(tareas):
    """Imprime todas las tareas pendientes con su posicion numerica."""
    print_list(tareas)


def menu():
    print("\n=== Todo List ===")
    print("1. Agregar tarea")
    print("2. Mostrar tareas pendientes")
    print("3. Eliminar tarea")
    print("4. Salir")


def main():
    tareas = []

    while True:
        menu()
        opcion = input("Elegi una opcion: ").strip()

        if opcion == "1":
            titulo = input("Titulo de la nueva tarea: ")
            try:
                agregar_tarea(tareas, titulo)
                print("Tarea agregada.")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "2":
            mostrar_tareas(tareas)

        elif opcion == "3":
            mostrar_tareas(tareas)
            if tareas:
                pos = input("Posicion a eliminar: ").strip()
                try:
                    eliminada = eliminar_tarea(tareas, int(pos))
                    print(f"Tarea eliminada: {eliminada}")
                except (ValueError, IndexError) as e:
                    print(f"Error: posicion invalida ({e})")

        elif opcion == "4":
            print("Chau!")
            break

        else:
            print("Opcion invalida.")


if __name__ == "__main__":
    main()
