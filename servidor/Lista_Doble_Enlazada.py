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

    def agregar_inicio(self, dato,password,direccion,telefono,edad):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato,password,direccion,telefono,edad)
        else:
            aux = Nodo(dato,password,direccion,telefono,edad)
            aux.siguiente = self.primero
            self.primero.anterior = aux
            self.primero = aux
        self.__unir_nodos()
        return True

    def agregar_final(self,dato,password,direccion,telefono,edad):
        if self.vacia():
            self.primero=self.ultimo=Nodo(dato,password,direccion,telefono,edad)
        else:
            aux= self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato,password,direccion,telefono,edad)
            self.ultimo.anterior = aux
        self.__unir_nodos()
        return True
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
#------------------------ busca todos los datos de una persona
    def buscar(self,dato):
        cadena =False
        aux = self.primero
        while aux:
            if aux.dato == dato:

                cadena = "Usuario : "+aux.dato +"  Password: "+aux.password+"  Direccion : "+ aux.direccion+"  Telefono : "+ aux.telefono+"  Edad : "+aux.edad
                print cadena
                return cadena
            else:
                aux = aux.siguiente
                if aux == self.primero:
                    print False
                    return False


#----------------------------- busca y compara si el usuario existe y si su contrasena es valida

    def buscarusuario(self, dato, passw):
        cadena = False
        aux = self.primero
        while aux:
             if aux.dato == dato and aux.password == passw:
                  cadena = True
                  print cadena
                  return cadena

             else:
                 aux = aux.siguiente
                 if aux == self.primero:
                     cadena = False
                     print cadena
                     return  cadena


                #------------ Modificar usuario

    def modificarusuario(self, dato,nuevo):  # puede modificar el nombre del usuario
        aux = self.primero
        while aux:
            if aux.dato == dato:
                aux.dato=nuevo
                return True
            else:
                aux = aux.siguiente
                if aux == self.primero:
                    return False
#------------------------------modificar password
    def modificarpassword(self, dato,nuevo):
        aux = self.primero
        while aux:
            if aux.dato == dato:
                aux.password=nuevo
                return True
            else:
                aux = aux.siguiente
                if aux == self.primero:
                    return False
#---------------------- modificar direccion
    def modificardireccion(self, dato,nuevo):
        aux = self.primero
        while aux:
            if aux.dato == dato:
                aux.direccion=nuevo
                return True
            else:
                aux = aux.siguiente
                if aux == self.primero:
                    return False
#-----------------------modificiar telefono
    def modificartelefono(self, dato,nuevo):
        aux = self.primero
        while aux:
            if aux.dato == dato:
                aux.telefono=nuevo
                return True
            else:
                aux = aux.siguiente
                if aux == self.primero:
                    return False

#------------------------- modificiar edad
    def modificaredad(self, dato,nuevo):
        aux = self.primero
        while aux:
            if aux.dato == dato:
                aux.edad=nuevo
                return True
            else:
                aux = aux.siguiente
                if aux == self.primero:
                    return False



    def recorrer_inicio_a_fin(self):
        aux = self.primero
        while aux:
            cadena = "Usuario : " + aux.dato + "  Password: " + aux.password + "  Direccion : " + aux.direccion + "  Telefono : " + aux.telefono + "  Edad : " + aux.edad
            print cadena
            print (aux.dato)
            aux = aux.siguiente
            if aux == self.primero:
                break

    def recorrer_fin_a_inicio(self):
        aux = self.ultimo
        while aux:
            print (aux.dato)
            print (aux.password)
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
    l.agregar_inicio("pablo","1232"," 4 ta avenidia","24338532","25")
    l.agregar_inicio("hoa","2"," 4 ta avenidia","24338532","20")
    l.agregar_inicio("hla","3"," 4 ta avenidia","24338532","2")
    l.agregar_inicio("ho","4"," 4 ta avenidia","24338532","25\7")
    l.modificarusuario("hla","luis")
    l.modificarpassword("ho","pass")
    l.modificardireccion("hoa","mixco")
    l.modificartelefono("pablo","41414141")
    l.modificaredad("ho","15")
    l.recorrer_inicio_a_fin()
    l.graficar()
    l.eliminar_inicio()
    l.eliminar_ultimo()

    l.buscar("hl")
    l.buscarusuario("hla", "54")
