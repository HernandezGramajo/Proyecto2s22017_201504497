from Matriz import MatrizDispersa
#from Arbolf import ArbolAVL
from flask import Flask, request, Response,render_template
from Lista_Doble_Enlazada import  ListaCircularDobleEnlazada
from Lista_simple_circular import ListasimpleCicular
from ArbolAVL import ArbolAVL
from Arbol_B import ArbolB

listadoble = ListaCircularDobleEnlazada()
listasimple = ListasimpleCicular()
arbolb=ArbolB()
avl = ArbolAVL()
app = Flask(__name__)

class principal():
    global lista
    global matriz
    matriz = MatrizDispersa()


    @app.route('/') 
    def metodo1():
      return "WEB SERVICE PROYECTO 2 "
#------------------------------------ Lista doble enlazada y su medos
    @app.route('/registro', methods=['POST'])
    def metodo2():

        usuario = str(request.form['usuario'])
        password = str(request.form['password'])
        direccion = str(request.form['direccion'])
        telefono = str(request.form['telefono'])
        edad = str(request.form['edad'])

        respuesta =listadoble.agregar_inicio(usuario,password,direccion,telefono,edad) # falta agregar datos a la lista doble
        print ("datos ingresado correctamente "+respuesta )
        return respuesta

    @app.route('/modifica_usuario', methods=['POST'])
    def metodo3():

        usuario = str(request.form['usuario'])
        nuevo = str(request.form['nuevo'])

        respuesta =listadoble.modificarusuario(usuario,nuevo)
        print ("datos ingresado correctamente "+respuesta )
        return respuesta

    @app.route('/modifica_password', methods=['POST'])
    def metodo4():

        usuario = str(request.form['usuario'])
        nuevo = str(request.form['nuevo'])

        respuesta = listadoble.modificarpassword(usuario, nuevo)
        print ("datos ingresado correctamente " + respuesta)
        return respuesta

    @app.route('/modifica_direccion', methods=['POST'])
    def metodo5():

        usuario = str(request.form['usuario'])
        nuevo = str(request.form['nuevo'])

        respuesta = listadoble.modificardireccion(usuario, nuevo)
        print ("datos ingresado correctamente " + respuesta)
        return respuesta

    @app.route('/modifica_telefono', methods=['POST'])
    def metodo6():

        usuario = str(request.form['usuario'])
        nuevo = str(request.form['nuevo'])

        respuesta = listadoble.modificartelefono(usuario, nuevo)
        print ("datos ingresado correctamente " + respuesta)
        return respuesta

    @app.route('/modifica_edad', methods=['POST'])
    def metodo7():

        usuario = str(request.form['usuario'])
        nuevo = str(request.form['nuevo'])

        respuesta = listadoble.modificaredad(usuario, nuevo)
        print ("datos ingresado correctamente " + respuesta)
        return respuesta

    @app.route('/eliminar_inicio', methods=['POST'])
    def metodo8():

        respuesta = listadoble.eliminar_inicio()
        print ("elimminado incio" + respuesta)
        return respuesta

    @app.route('/eliminar_fin', methods=['POST'])
    def metodo9():

        respuesta = listadoble.eliminar_ultimo()
        print ("eliminado ultimo " + respuesta)
        return respuesta


    @app.route('/ingreso', methods=['POST'])  # verifica si el usuario existe
    def metodo10():

        usuario = str(request.form['usuario'])
        password = str(request.form['password'])

        respuesta =listadoble.buscarusuario(usuario, password)
        print ("contra verificada " + respuesta)
        return respuesta

    @app.route('/graficar_lista_doble', methods=['POST'])  # verifica si el usuario existe
    def metodo11():

        respuesta =listadoble.graficar()
        print ("graficando lista doble" )
        return respuesta



#----------------------------//////-- fin lista doble enlazada ---------////////////////


#--------------------------- inicio  de metodos de lista simple circular--------------
    @app.route('/habitacioneslista', methods=['POST'])
    def metodo12():

        nivel= "Nivel "+str(request.form['nivel'])
        numero = "Habitacion "+str(request.form['numero'])
        codigo = str(nivel+numero)

        listasimple.agregar_inicio(codigo,nivel,numero)

        print ("habitaciones en lista")
        return "True"

    @app.route('/habitacion_eliminar_inicio', methods=['POST'])
    def metodo13():


        listasimple.eliminar_inicio()

        print ("habitacion de inicio eliminada")
        return "True"

    @app.route('/habitacion_eliminar_fin', methods=['POST'])
    def metodo14():

        listasimple.eliminar_ultimo()

        print ("habitacion de ultimo eliminada")
        return "True"

    @app.route('/graficar_lista_simple', methods=['POST'])
    def metodo15():

        respuesta =listasimple.graficar()

        print ("graficando lista simple")
        return respuesta
##-------------------------- //// fin de metodos de lista simple circular---------------------

#------------------------ METDOS DE ARBOL B------------------------


    @app.route('/bitacora', methods=['POST']) #INGRESA BITACORA
    def metodo16():

        calave = str(request.form['fecha'])
        bitacora = str(request.form['bitacora'])

        respuesta = arbolb.insertar(calave, bitacora)

        print ("ingresa datos en arbo b")
        return respuesta

    @app.route('/modificar_bitacora', methods=['POST']) # MODIFICA LA BITACORA
    def metodo17():

        calave= str(request.form['fecha'])
        bitacora = str(request.form['bitacora'])

        respuesta =arbolb.modifica(calave,bitacora)

        print ("bitacora del arbol b modificada")
        return respuesta

    @app.route('/modifica_clave_bitacora', methods=['POST']) # modifica la clave pero no lo valancea no se que ondas
    def metodo18():

        calave = str(request.form['fecha'])
        nueva = str(request.form['clave'])

        respuesta = arbolb.modificaclave(calave, nueva)

        print ("clave del arbol b modificada")
        return respuesta

    @app.route('/graficar_arbolB', methods=['POST']) # modifica la clave pero no lo valancea no se que ondas
    def metodo19():

        respuesta = arbolb.imprimir_arbol()

        print (" graficando arbol b")
        return respuesta

#-----------------------/// FIn medotos del ARBOL B-------------------------

#------------------------INICIO DE METODOS DEL AVL-----------------------

    @app.route('/gastos_avl', methods=['POST'])
    def metodo20():

        cuenta= str(request.form['cuenta'])
        monto = str(request.form['monto'])

        avl.insertar(cuenta,monto)

        print ("monto y cuenta ingresado al avl")
        return "True"


    @app.route('/modificar_gastos', methods=['POST'])
    def metodo21():

        cuenta= str(request.form['cuenta'])
        nuevo = str(request.form['monto'])

        avl.insertar(cuenta,nuevo) #----------------------------cambiar por medo modificar avl gastos

        print ("monto modificado al avl")
        return "True"


    @app.route('/modificar_cuenta', methods=['POST'])
    def metodo22():

        cuenta= str(request.form['cuenta'])
        nuevo = str(request.form['cuenta'])

        avl.insertar(cuenta,nuevo) #----------------------------cambiar por medo modificar avl cuenta

        print ("cuenta modificada avl")
        return "True"

    @app.route('/eliminar_cuenta', methods=['POST'])
    def metodo23():

        cuenta = str(request.form['cuenta'])

        avl.eliminar(cuenta)  # ----------------------------cambiar por metodo eliminar avl cuenta

        print ("cuenta eliminada avl")
        return "True"

    @app.route('/graficar_avl', methods=['POST'])
    def metodo24():

        avl.graficar()  # ----------------------------componer metodo graficar

        print ("graficando  avl")
        return "True"
#------------------------/// Fin de metodos avl-------------------------------------------------------------------------


#----------------------------------inicio metodos de matriz dispersa----------------

    @app.route('/reservar',methods=['POST'])
    def metodo25():
        parametro1 = str(request.form['mes'])
        parametro2 = str(request.form['ano'])
        parametro3 = str(request.form['dia'])

        texto = ""
        if(matriz.verificarExistencia(parametro1,parametro2,parametro3)==0):
            encabezadomes= matriz.insertar(parametro1)
            encabezadofecha = matriz.insertar1(parametro2)
            Nodo = matriz.insertarValor(encabezadomes,parametro3,parametro2,parametro3)
            matriz.unir(encabezadofecha,Nodo)
            texto = "SI"
        else:
            texto = "NO" # ya existe
        return texto


    @app.route('/graficar_matrizdis',methods=['POST'])
    def metodo26():

       respuesta= matriz.getCodigoGraphviz()
       return respuesta

#---------------------------------/// fin matriz dispersa----------------

# -----------------------inicio medotodos para la tabla hash----------------


    if __name__ == "__main__":
        app.run(debug=True, host='0.0.0.0')

