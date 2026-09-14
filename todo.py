#!/usr/bin/env python3
"""Herramienta de terminal ligera para gestionar una lista de tareas (todos).

Funcionalidades:
- Agregar una nueva tarea por titulo
- Mostrar todas las tareas pendientes con su posicion numerica
- Eliminar una tarea por su posicion en la lista
- Guardar tareas en un archivo todos.csv
- Cargar nuevamente las tareas desde todos.csv

No se soporta edicion de tareas: para modificar una tarea, se debe
eliminar y volver a crear.
"""

import csv
import os

CSV_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "todos.csv")
CSV_HEADER = ["titulo"]


def load_todos(path=CSV_FILE):
    """Carga de forma persistente la lista de tareas desde el archivo todos.csv.

    Devuelve una lista de titulos. Si el archivo no existe, devuelve una
    lista vacia.
    """
    tareas = []
    if not os.path.exists(path):
        return tareas

    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)

    if not rows:
        return tareas

    # Si la primera fila es el encabezado, se omite.
    start = 1 if rows[0] == CSV_HEADER else 0
    for row in rows[start:]:
        if row:
            tareas.append(row[0])
    return tareas


def cargar_tareas(path=CSV_FILE):
    """Carga las tareas desde el archivo CSV y devuelve una lista de titulos."""
    return load_todos(path)


def save_todos(tareas, path=CSV_FILE):
    """Guarda de forma persistente la lista de tareas en el archivo todos.csv."""
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(CSV_HEADER)
        for titulo in tareas:
            writer.writerow([titulo])


def guardar_tareas(tareas, path=CSV_FILE):
    """Guarda la lista de tareas en el archivo CSV."""
    save_todos(tareas, path)


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
    print("4. Guardar tareas en todos.csv")
    print("5. Cargar tareas desde todos.csv")
    print("6. Salir")


def main():
    tareas = cargar_tareas()

    while True:
        menu()
        opcion = input("Elegi una opcion: ").strip()

        if opcion == "1":
            print("Ingresa el titulo de cada tarea (una por linea).")
            print("Dejar la linea vacia para terminar de agregar tareas.")
            cantidad_agregadas = 0
            while True:
                titulo = input(f"Titulo de la tarea #{cantidad_agregadas + 1} (vacio para terminar): ")
                if titulo.strip() == "":
                    break
                try:
                    add_one_task(titulo, tareas)
                    cantidad_agregadas += 1
                    print(f"Tarea agregada: {titulo.strip()}")
                except ValueError as e:
                    print(f"Error: {e}")
            print(f"Se agregaron {cantidad_agregadas} tarea(s).")

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
            save_todos(tareas)
            print(f"Tareas guardadas en {CSV_FILE}")

        elif opcion == "5":
            tareas = load_todos()
            print("Tareas cargadas desde todos.csv")

        elif opcion == "6":
            print("Chau!")
            break

        else:
            print("Opcion invalida.")


if __name__ == "__main__":
    main()
