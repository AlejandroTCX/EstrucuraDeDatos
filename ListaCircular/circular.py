import nodo


class Lista_Circular:
    def __init__(self):
        self.PrimerNodo = None
        self.UltimoNodo = None
        self.Auxiliar = None

    def Vacia(self):
    if self.PrimerNodo == None:
            return True
        else:
            return False

    def Agregar_Primer_Nodo(self, NodoAux):
        NodoAux.SigNodo = NodoAux
        self.PrimerNodo = NodoAux
        self.UltimoNodo = NodoAux
        self.Auxiliar = NodoAux

    def Agregar_Principio_Nodo(self, valor):
        nodoAux = nodo.Nodo(valor)
        if self.Vacia():
            self.Agregar_Primer_Nodo(nodoAux)
        else:
            nodoAux.SigNodo = self.PrimerNodo
            self.UltimoNodo.SigNodo = nodoAux
            self.PrimerNodo = nodoAux

    def Agregar_Ulitimo_Nodo(self, valor):
        nodoAux = nodo.Nodo(valor)
        if self.Vacia():
            self.Agregar_Primer_Nodo(nodoAux)
        else:
            self.Auxiliar = self.PrimerNodo
            while(self.Auxiliar.SigNodo != self.PrimerNodo):
                self.Auxiliar = self.Auxiliar.SigNodo
            self.Auxiliar.SigNodo = nodoAux
            nodoAux.SigNodo = self.PrimerNodo
            self.UltimoNodo = nodoAux

    def Agregar_Medio_Nodo(self, valor, nodoBuscado):
        nodoAux = nodo.Nodo(valor)
        if self.Vacia():
            self.Agregar_Primer_Nodo(nodoAux)
        elif self.Buscar_Nodo(nodoBuscado) == 0:
            self.Agregar_Ulitimo_Nodo(valor)
        else:
            self.Auxiliar = self.PrimerNodo
            while (self.Auxiliar.SigNodo != self.PrimerNodo):
                if self.Auxiliar.Valor == nodoBuscado:
                    nodoAux.SigNodo = self.Auxiliar.SigNodo
                    self.Auxiliar.SigNodo = nodoAux
                    return
                self.Auxiliar = self.Auxiliar.SigNodo
            if self.Auxiliar.Valor == nodoBuscado:
                self.Agregar_Ulitimo_Nodo(valor)

    def Imprimir_Lista(self):
        if self.Vacia():
            print("La lista se encuentra vacia")
            return
        elif self.PrimerNodo == self.UltimoNodo:
            print(self.PrimerNodo.Valor)
        else:
            self.Auxiliar = self.PrimerNodo
            while(self.Auxiliar.SigNodo != self.PrimerNodo):
                print(self.Auxiliar.Valor, end=", ")
                self.Auxiliar = self.Auxiliar.SigNodo
            print(self.Auxiliar.Valor)

    def Eliminar_Nodo(self, valor):
  
        if self.Buscar_Nodo(valor) == 0:
            print("El valor no se encuetra en la lista")


        elif self.PrimerNodo == self.UltimoNodo and self.Buscar_Nodo(valor) == 1:
            del self.PrimerNodo
            self.PrimerNodo = None
            self.UltimoNodo = None
            self.Auxiliar = None

 
        elif self.PrimerNodo.Valor == valor:
            self.Auxiliar = self.PrimerNodo.SigNodo
            self.UltimoNodo.SigNodo = self.Auxiliar
            self.PrimerNodo.SigNodo = None
            self.PrimerNodo = self.Auxiliar


        elif self.UltimoNodo.Valor == valor:
            self.Auxiliar = self.PrimerNodo
            while(self.Auxiliar.SigNodo != self.UltimoNodo):
                self.Auxiliar = self.Auxiliar.SigNodo
            self.Auxiliar.SigNodo = self.PrimerNodo
            self.UltimoNodo.SigNodo = None
            self.UltimoNodo = self.Auxiliar

        else:
            self.Auxiliar = self.PrimerNodo
            while (self.Auxiliar.SigNodo != self.PrimerNodo):
                if self.Auxiliar.Valor == valor:
                    anterior_nodo = self.Auxiliar
                    while(anterior_nodo.SigNodo != self.Auxiliar):
                        anterior_nodo = anterior_nodo.SigNodo
                    eliminar_temporal = anterior_nodo.SigNodo.SigNodo
                    anterior_nodo.SigNodo.SigNodo = None
                    anterior_nodo.SigNodo = eliminar_temporal
                    return
                self.Auxiliar = self.Auxiliar.SigNodo

    def Eliminar_Nodos_Repetidos(self):
        if self.Vacia():
            print("La lista se encuentra vacia")
            return
        elif self.PrimerNodo == self.UltimoNodo:
            print("La lista solo contiene un nodo")
            return
        else:
            Encontro = False
            self.Auxiliar = self.PrimerNodo
            while(self.Auxiliar.SigNodo != self.PrimerNodo):
                next_temp = self.Auxiliar.SigNodo
                if self.Buscar_Nodo(self.Auxiliar.Valor) > 1:
                    Encontro = True
                    temp_eliminar = self.Auxiliar
                    while(self.Buscar_Nodo(temp_eliminar.Valor) != 0):
                        self.Eliminar_Nodo(temp_eliminar.Valor)
                self.Auxiliar = next_temp
            if not Encontro:
                print("No se encontraron valores repetidos")

    def Buscar_Nodo(self, valor):
        if self.Vacia():
            return 0
        elif self.PrimerNodo == self.UltimoNodo and self.PrimerNodo.Valor == valor:
            return 1
        else:
            temp = self.PrimerNodo
            contador = 0
            while(temp.SigNodo != self.PrimerNodo):
                if temp.Valor == valor:
                    contador += 1
                temp = temp.SigNodo
            return (contador, contador+1)[temp.Valor == valor]
