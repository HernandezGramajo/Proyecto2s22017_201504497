
class NodoAVL(object):
    def __init__(self, cuenta,monto):
        self._correlativo = 1
        self.cuenta = cuenta#Este es el atributo id (pero con otro nombre...)
        self.monto = monto

        self._izquierdo = None
        self._altura=0
        self._derecho = None
        self._id = self._correlativo =self._correlativo+1

    def insertar(self, val):
        if val.compareTo(self._valor) < 0:
            if self._izquierdo == None:
                self._izquierdo = NodoAVL(val)
            else:
                self._izquierdo.insertar(val)
        elif val.compareTo(self._valor) > 0:
            if self._derecho == None:
                self._derecho = NodoAVL(val)
            else:
                self._derecho.insertar(val)
        else:
            print("No se permiten los valores duplicados: \"" + str.valueOf(val) + "\".")

    def getCodigoGraphviz(self):
        return "digraph grafica{\n" + "rankdir=TB;\n" + "node [shape = record, style=filled, fillcolor=seashell2];\n" + self.getCodigoInterno() + "}\n"

    def getCodigoInterno(self):
        if self._izquierdo == None and self._derecho == None:
            etiqueta = "nodo1" + " [ label =\"" + self.cuenta+"\n"+self.monto+"\n"+ "\"];\n"
        else:
            etiqueta = "nodo2"  + " [ label =\"<C0>|" + self.cuenta + "|<C1>\"];\n"
        if self._izquierdo != None:
            etiqueta = etiqueta + self._izquierdo.getCodigoInterno() + "nodo1"  ":C0->nodo" + str(self._izquierdo._id) + "\n"
        if self._derecho != None:
            etiqueta = etiqueta + self._derecho.getCodigoInterno() + "nodo2" ":C1->nodo" + str(self._derecho._id) + "\n"
        return etiqueta



