

class node():
    def __init__(self, dato):
        self.left = None
        self.right = None
        self.dato = dato

class arbol():
    def __init__(self):
        self.root = None
        
    def insert(self, a, dato):
        if a == None:
            a = node(dato)
        else:
            d = a.dato
            if dato < d:
                a.left = self.insert(a.left, dato)
            else:
                a.right = self.insert(a.right, dato)
        return a

    def inorder(self, a):
        if a == None:
            return None
        else:
            self.inorder(a.left)
            print(a.dato)
            self.inorder(a.right)



    def buscar(self, dato, a):
        if a == None:
            return None
        else:
            if dato == a.dato:
                return a.dato
            else:
                if dato < a.dato:
                    return self.buscar(dato, a.left)
                else:
                    return self.buscar(dato, a.right)

tree = arbol()

while True:
  
    print("Árbol Binario Inorden")
    opc = input("\n1.-Insertar nodo \n2.-Buscar Nodo \n3.-Imprimir árbol en Inorden \n4.-Salir \n \n\nElige una opcion:  ")

    if opc == '1':
        nodo = input("\nIngresa el nodo:  ")
        if nodo.isdigit():
            nodo = int(nodo)
            tree.root = tree.insert(tree.root, nodo)
         
                
        else:
            print("\nIngresa solo digitos ")
    elif opc == '3':
        if tree.root == None:
            print("Vacio")
        else:
            tree.inorder(tree.root)
  
    
    elif opc == '2':
        nodo = input("\nIngresa el nodo a buscar: ")
        if nodo.isdigit():
            nodo = int(nodo)
            if tree.buscar(nodo, tree.root) == None:
                print("\nNodo no encontrado ")
            else:
                print("\nNodo encontrado  ",tree.buscar(nodo, tree.root), " si existe  ")
        else:
            print("\nIngresa solo digitos ")        
    elif opc == '4':
        print("\nElegiste salir \n")
   
        break
    else:
        print("\nElige una opcion correcta ")
    print()
   
