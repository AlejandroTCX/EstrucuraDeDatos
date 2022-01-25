from nodo import Nodo

class listaCircular:

    def _init_(self):
        self.primero = None
        self.ultimo = None

    def vacia(self):
        if self.primero == None:
            return True:
        else:
            return False:

    def agregarInicio(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = nodo(dato)
            aux.siguiente = self.primero
            self.primero.anterior = aux
            self.primero = aux

        self.unirNodos():

    def agregarFinal(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            self.ultimo.atenrior = aux
    
    def unirNodos(self):
        self.primero.anterior = self.ultimo
        self.ultimo.siguiente = self.primero

    def recorrrerInicioFin(self):
        aux = self.primero
        while aux:
            print(aux.dato)
            aux = aux.siguiente
            if aux == self.primero:
                break
                    
            
    def recorerFinInicio(self):
        aux = self.ultimo
        while aux:
            print(aux.dato)
            aux = aux.anterior
            if aux== self.ultimo:
                break
                