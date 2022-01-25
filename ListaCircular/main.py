import os
import lista_Circular


def menu():
    datos_menu = "Lista circular simple\n\t1. Agregar un nodo al inicio\n\t2. Agregar un nodo al final\n\t3. Agregar un nodo en medio\n\t4. Eliminar un nodo\n\t5. Imprimir la lista\n\t6. Eliminar nodos repetidos\n\t7. Salir"
    print(datos_menu)


def main():
    lista = lista_Circular.Lista_Circular()

    val_menu = 0
    while(val_menu != 7):
        menu()
        val_menu = int(input('Opcion: '))
        os.system('clear')

        if val_menu == 1:
            print("\tAgegar un nodo al inicio: ")
            valor = int(input('Ingresa el valor: '))
            lista.Agregar_Principio_Nodo(valor)

        elif val_menu == 2:
            print("\tAgegar un nodo al final: ")
            valor = int(input('Ingresa el valor: '))
            lista.Agregar_Ulitimo_Nodo(valor)

        elif val_menu == 3:
            print("\tAgrega un nodo en medio: ")
            valor = int(input('Ingresa el valor: '))
            nodo_valor = int(input('Ingresa el valor del nodo: '))
            lista.Agregar_Medio_Nodo(valor, nodo_valor)

        elif val_menu == 4:
            print("\tElimina un nodo: ")
            if lista.Vacia():
                print("La lista se encuentra vacia")
            else:
                valor = int(input('Ingresa el valor: '))
                lista.Eliminar_Nodo(valor)

        elif val_menu == 5:
            print("\tImprimir la Lista: ")
            lista.Imprimir_Lista()

        elif val_menu == 6:
            print("\tEliminar nodos repetidos: ")
            lista.Eliminar_Nodos_Repetidos()

        elif val_menu == 7:
            print("\tSalir del sistema")

        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()
