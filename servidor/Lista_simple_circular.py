from Nodo_Lista_simple_circular import Nodo

class ListasimpleCicular:

    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacia(self):
        if self.primero == None:
            return  True
        else:
            return False

    def agregar_inicio(self, dato,nivel,habitacion):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato,nivel,habitacion)
        else:
            aux = Nodo(dato,nivel,habitacion)
            aux.siguiente = self.primero
            self.primero.anterior = aux
            self.primero = aux
        self.__unir_nodos()

    def agregar_final(self,dato,nivel,habitacion):
        if self.vacia():
            self.primero=self.ultimo=Nodo(dato,nivel,habitacion)
        else:
            aux= self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato,nivel,habitacion)
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
            texto += str(cont) +"[label =\""  +aux.nivel+"\n" + aux.habitacion+"\n"+ aux.dato + "\"];\n"

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

            con = con+1
            if con+1 == cont:

                texto += str(cont) + "->0"+ ";\n"



        return texto

    def graficar(self):
        texto = "digraph grafica{\n" + "rankdir=LR;\n" + "node [shape = ellipse, style=filled, fillcolor=seashell2];\n" + self.graficar_inicio_a_fin() + "}\n"
        print texto
        return texto
if __name__ == "__main__":
    l = ListasimpleCicular() # insertar al final

    l.agregar_inicio("nivel 1"," numero 7"," 17")
    l.agregar_inicio("nivel 1"," numero 8 "," 18")
    l.agregar_inicio("nivel 4"," numero 7 "," 47")
    l.agregar_inicio("nivel 1","numero 70 "," 170")
    l.agregar_inicio("nivel 5"," numero 7 ","57")
    l.agregar_inicio("nivel 3","numero 27 "," 327")
    l.graficar()
    l.eliminar_inicio()
    l.graficar()