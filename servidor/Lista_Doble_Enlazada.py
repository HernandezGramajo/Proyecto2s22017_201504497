from Nodo_Lista_Doble import Nodo

class ListaCircularDobleEnlazada:

    def __init__(self):
        self.primero = None
        self.ultimo = None


    def vacia(self):
        if self.primero == None:
            return  True
        else:
            return False

    def agregar_inicio(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero.anterior = aux
            self.primero = aux
        self.__unir_nodos()

    def agregar_final(self,dato):
        if self.vacia():
            self.primero=self.ultimo=Nodo(dato)
        else:
            aux= self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            self.ultimo.anterior = aux
        self.__unir_nodos()

    def __unir_nodos(self):
        if self.primero !=None:
            self.primero.anterior = self.ultimo
            self.ultimo.siguiente = self.primero


    def eliminar_inicio(self):
        if self.vacia():
            print ("Tu estructura esta vacia")
        elif self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            self.primero = self.primero.siguiente
        self.__unir_nodos()

    def eliminar_ultimo(self):
        if self.vacia():
            print ("Tu estructura esta vacia")
        elif self.primero == self.ultimo:
            self.primero = self.ultimo =None
        else:
            self.ultimo = self.ultimo.anterior
        self.__unir_nodos()

    def buscar(self,dato):
        aux = self.primero
        while aux:
            if aux.dato == dato:
                print aux.dato

                return True
            else:
                aux = aux.siguiente
                if aux == self.primero:
                    return False

    def modificar(self, dato,nuevo):  # puede modificar el nombre del usuario
        aux = self.primero
        while aux:
            if aux.dato == dato:
                aux.dato=nuevo
                return True
            else:
                aux = aux.siguiente
                if aux == self.primero:
                    return False



    def recorrer_inicio_a_fin(self):
        aux = self.primero
        while aux:
            print (aux.dato)
            aux = aux.siguiente
            if aux == self.primero:
                break

    def recorrer_fin_a_inicio(self):
        aux = self.ultimo
        while aux:
            print (aux.dato)
            aux = aux.anterior
            if aux == self.ultimo:
                break
    def graficar_inicio_a_fin(self):
        aux = self.primero
        texto=""
        cont =0
        while aux:
            texto += str(cont) +"[label =\"" + aux.dato + "\"];\n"

            aux = aux.siguiente

            if aux == self.primero:

                 break
            else:
             cont = cont + 1


        con = 0

        while (con<cont):
            l =con +1
            print  con
            texto += str(con) + "->" + str(l) + ";\n"
            texto += str(l) + "->" + str(con) + ";\n"
            con = con+1



        return texto

    def graficar(self):
        texto = "digraph grafica{\n" + "rankdir=LR;\n" + "node [shape = ellipse, style=filled, fillcolor=seashell2];\n" + self.graficar_inicio_a_fin() + "}\n"
        print texto
        return texto


if __name__ == "__main__":
    l = ListaCircularDobleEnlazada()
    l.agregar_inicio("hola")
    l.agregar_inicio("hoa")
    l.agregar_inicio("hla")
    l.agregar_inicio("ho")


    l.graficar()
    #l.modificar("1","luis")
    #l.eliminar_inicio()
    #l.graficar()