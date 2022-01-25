import nodo


class Cola:
    def __init__(self):
        self.PrimerNodo = None
        self.UltimoNodo = None
        self.Auxiliar = None

    def Vacia(self):
        if self.PrimerNodo == None:
            return True
        else:
            return False

    def Agregar_Nodo(self, valor):
        NodoAux = nodo.Nodo(valor)

        # Nodo= Valor = valor, SigNodo = None
        if self.Vacia():
            self.PrimerNodo = NodoAux
            self.UltimoNodo = NodoAux
            self.Auxiliar = NodoAux

        else:
            # Nodo Valor = balor , SigNodo = None
            NodoAux.SiguienteNodo = self.PrimerNodo
            # Nodo Valor = valor, SigNodo  = Self.PrimerNodo
            self.PrimerNodo = NodoAux

    def Eliminar_Nodo(self):
        if self.Vacia():
            print("La lista se encuentra vacia")
        elif self.PrimerNodo == self.UltimoNodo:
            del self.PrimerNodo
            self.PrimerNodo = None
            self.Auxiliar = None
            self.UltimoNodo = None
        else:
            self.Auxiliar = self.PrimerNodo
            while self.Auxiliar.SiguienteNodo != self.UltimoNodo:
                self.Auxiliar = self.Auxiliar.SiguienteNodo
            self.UltimoNodo = self.Auxiliar
            self.UltimoNodo.SiguienteNodo = None

    def Imprimir_Cola(self):
        if self.Vacia():
            print("La lista se encuentra vacia")
            return
        else:
            self.Auxiliar = self.PrimerNodo
            while self.Auxiliar.SiguienteNodo != None:
                print(self.Auxiliar.Valor, end=", ")
                self.Auxiliar = self.Auxiliar.SiguienteNodo
            print(self.Auxiliar.Valor)





