
from NodoAVL import NodoAVL
class ArbolAVL(object):
	def __init__(self):
		self._raiz = None
		self._Lista = None
		self._auxmonto = None

		self._tempId = None

	def insertar(self, cuenta,monto):
		self._raiz = self.insertar1(cuenta,monto, self._raiz)

	def graficar(self):
		texto = self._raiz.getCodigoGraphviz()
		print("--------------------")
		print(texto)

	def inorden(self):
		print("Recorrido inorden del arbol binario de busqueda:")
		self.inorden1(self._raiz)
		print("")

	def inorden1(self, a):
		if a == None:
			return
		self.inorden1(a._izquierdo)
		print(a.cuenta + ",")
		self.inorden1(a._derecho)

	def obtenerListaIds(self):
		self._Lista = []
		self.obtenerListaIds1(self._raiz)
		print("TAMAnio "+str(len(self._Lista)))

	def obtenerListaIds1(self, a):
		if a == None:
			return
		self.obtenerListaIds1(a._izquierdo)
		self._Lista.append(a.cuenta)
		print("--------"+a.cuenta)
		self.obtenerListaIds1(a._derecho)

	def obtenerDatos(self,id):
		self._tempId = id
		self._auxmonto =""
		self.obtenerDatos1(self._raiz)

	def obtenerDatos1(self, a):
		if a == None:
			return
		if(a.cuenta == self._tempId):
			print("Supuestamente entre hahaha")
			print(a.monto)

			self._auxmonto =a.monto

		self.obtenerDatos1(a._izquierdo)
		self.obtenerDatos1(a._derecho)
	def actualizarDatos(self,id,monto):
		self._tempId = id
		self._auxmonto =monto
		self.actualizarDatos1(self._raiz)

	def actualizarDatos1(self, a):
		if a == None:
			return
		else:
			if(a.cuenta == self._tempId):
				a.monto=self._auxmonto
		self.actualizarDatos1(a._izquierdo)
		self.actualizarDatos1(a._derecho)
	def insertar1(self, cuenta,monto, raiz):
		if raiz == None:
			raiz = NodoAVL(cuenta,monto)
			#print("inserte "+raiz._valor)
		elif self.compareTo(cuenta,raiz.cuenta) < 0:
			raiz._izquierdo = self.insertar1(cuenta,monto,raiz._izquierdo)
			if self.altura(raiz._derecho) - self.altura(raiz._izquierdo) == -2:
				if self.compareTo(cuenta,raiz._izquierdo.cuenta) < 0:
					raiz = self.IzquierdaIzquierda(raiz)
				else:
					raiz = self.IzquierdaDerecha(raiz)
		elif self.compareTo(cuenta,raiz.cuenta) > 0:
			raiz._derecho = self.insertar1(cuenta,monto, raiz._derecho)
			if self.altura(raiz._derecho) - self.altura(raiz._izquierdo) == 2:
				if self.compareTo(cuenta,raiz._derecho.cuenta) > 0:
					raiz = self.DerechaDerecha(raiz)
				else:
					raiz = self.DerechaIzquierda(raiz)
		else:
			print("No se permiten los valores duplicados: \"" + str(cuenta) + "\".")
		raiz._altura = self.mayor(self.altura(raiz._izquierdo), self.altura(raiz._derecho)) + 1
		return raiz
	def compareTo(self,x,y):
		bandera = 0
		temp=[x, y]
		temp.sort()
		if(x==y):
			bandera =0
		elif(temp.index(x)==0):
			bandera = -1
		elif(temp.index(x)==1):
			bandera = 1
		return bandera

	def altura(self, nodo):
		if nodo == None:
			return -1
		else:
			return nodo._altura

	def mayor(self, n1, n2):
		if n1 > n2:
			return n1
		return n2

	def IzquierdaIzquierda(self, n1):
		n2 = n1._izquierdo
		n1._izquierdo = n2._derecho
		n2._derecho = n1
		n1._altura = self.mayor(self.altura(n1._izquierdo), self.altura(n1._derecho)) + 1
		n2._altura = self.mayor(self.altura(n2._izquierdo), n1._altura) + 1
		return n2

	def DerechaDerecha(self, n1):
		n2 = n1._derecho
		n1._derecho = n2._izquierdo
		n2._izquierdo = n1
		n1._altura = self.mayor(self.altura(n1._izquierdo), self.altura(n1._derecho)) + 1
		n2._altura = self.mayor(self.altura(n2._derecho), n1._altura) + 1
		return n2

	def IzquierdaDerecha(self, n1):
		n1._izquierdo = self.DerechaDerecha(n1._izquierdo)
		return self.IzquierdaIzquierda(n1)

	def DerechaIzquierda(self, n1):
		n1._derecho = self.IzquierdaIzquierda(n1._derecho)
		return self.DerechaDerecha(n1)

if __name__ == "__main__":

    arbol = ArbolAVL()

    arbol.insertar("1234","silv")
    arbol.insertar("7415", "0s")
    arbol.insertar("8756", "pao")
    arbol.insertar("8856", "pablo5")
    arbol.insertar("2347", "pedro")
    arbol.obtenerDatos("8856")
    arbol.graficar()