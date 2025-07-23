import mysql.connector
from mysql.connector import Error
import os

borrar_pantalla = lambda: os.system("cls" if os.name == "nt" else "clear")
esperar_tecla = lambda: input("\nPresione cualquier tecla para continuar...")
crear_pelicula = lambda: print("\n\t¡PELÍCULA REGISTRADA CON ÉXITO!")
mostrar_peliculas = lambda: print("\n\tMostrando todas las películas...")
buscar_pelicula = lambda: print("\n\tBuscando película...")
actualizar_pelicula = lambda: print("\n\tActualizando película...")
eliminar_pelicula = lambda: print("\n\tEliminando película...")


def menu_principal():
    """Muestra el menú principal del sistema"""
    while True:
        borrar_pantalla()
        print("\n\t.:: SISTEMA DE GESTIÓN DE PELÍCULAS ::.")
        print("\n1. Registrar nueva película")
        print("2. Mostrar todas las películas")
        print("3. Buscar película")
        print("4. Actualizar película")
        print("5. Eliminar película")
        print("6. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            crear_pelicula()
        elif opcion == "2":
            mostrar_peliculas()
        elif opcion == "3":
            buscar_pelicula()
        elif opcion == "4":
            actualizar_pelicula()
        elif opcion == "5":
            eliminar_pelicula()
        elif opcion == "6":
            print("\n¡Hasta pronto!")
            break
        else:
            print("\nOpción no válida")
            esperar_tecla()

if __name__ == "__main__":
    menu_principal()
