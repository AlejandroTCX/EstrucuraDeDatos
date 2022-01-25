
import os
import cola


def menu():
    menu = "Menu\n\t1. Pila\n\t2. Cola\n\t3. Salir del programa"
    print(menu)


def pila_Menu():
    pila_menu = "PILA\n\t1. Agregar un elemento en la pila\n\t2. Borrar un elemento de la pila\n\t3. Imprimir la pila completa.\n\t4. Regresar al menu."
    print(pila_menu)


def cola_Menu():
    cola_menu = "PILA\n\t1. Agregar un elemento en la cola\n\t2. Borrar un elemento de la cola\n\t3. Imprimir la cola completa.\n\t4. Regresar al menu."
    print(cola_menu)


def main():
    Cola = cola.Cola()
    Pila = pila.Pila()
    val_menu = 0
    while(val_menu != 3):
        menu()
        val_menu = int(input('opcion: '))
        os.system('clear')
        if val_menu == 1:
            while(val_menu != 4):
                pila_Menu()
                val_menu = int(input('opcion: '))
                os.system('clear')

                if val_menu == 1:
                    print('\tAgregar un elemento a la pila')
                    valor = int(input('Ingresa el valor: '))
                    Pila.Agregar_Nodo(valor)

                elif val_menu == 2:
                    print('\tBorrar un elemento de la pila')
                    print('Se ha eliminado el primer elemento de la  pila')
                    Pila.Eliminar_Nodo()

                elif val_menu == 3:
                    print('\tImprimir la pila completa.')
                    Pila.Imprimir_Pila()

                elif val_menu == 4:
                    print('Regresando al menu principal')

                else:
                    print('Opcion no valido.')

        if val_menu == 2:
            while(val_menu != 4):
                cola_Menu()
                val_menu = int(input('opcion: '))
                os.system('clear')

                if val_menu == 1:
                    print('\tAgregar un elemento a la cola')
                    valor = int(input('Ingresa el valor: '))
                    Cola.Agregar_Nodo(valor)

                elif val_menu == 2:
                    print('\tBorrar un elemento de la cola')
                    print('Se ha eliminado el ultimo elemento de la  cola')
                    Cola.Eliminar_Nodo()

                elif val_menu == 3:
                    print('\tImprimir la cola completa.')
                    Cola.Imprimir_Cola()

                elif val_menu == 4:
                    print('Regresando al menu principal')

                else:
                    print('Opcion no valido.')


if __name__ == '__main__':
    main()
