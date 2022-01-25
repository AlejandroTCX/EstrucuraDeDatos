import nodo


class Pila:
    def __init__(self):
        self.__first = None
        self.__last = None
        self.__aux = None

    def Vacia(self):
        return (False, True)[self.__first == None]

    def Agregar_Nodo(self, valor):
        Nodo = nodo.Nodo(valor)
        if self.Vacia():
            self.__first = Nodo
            self.__last = Nodo
            self.__aux = Nodo
        else:
            Nodo.SigNodo = self.__first
            self.__first = Nodo

    def Eliminar_Nodo(self):
        if self.__first == self.__last:
            del self.__first
            self.__first = None
            self.__last = None
            self.__aux = None
        else:
            self.__aux = self.__first.SigNodo
            self.__first.SigNodo = None
            self.__first = self.__aux

    def Imprimir_Pila(self):
        if self.Vacia():
            print("La lista se encuentra vacia")
            return
        else:
            self.__aux = self.__first
            while self.__aux.SigNodo != None:
                print(self.__aux.Valor, end=", ")
                self.__aux = self.__aux.SigNodo
            print(self.__aux.Valor)
