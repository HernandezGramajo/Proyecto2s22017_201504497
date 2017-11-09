from Matriz import MatrizDispersa
#from Arbolf import ArbolAVL
from flask import Flask, request, Response,render_template
from Lista_Doble_Enlazada import  ListaCircularDobleEnlazada
from Lista_simple_circular import ListasimpleCicular
from ArbolAVL import ArbolAVL

listadoble = ListaCircularDobleEnlazada()
listasimple = ListasimpleCicular()
avl = ArbolAVL()
app = Flask(__name__)

class principal():
    global lista
    global matriz
    matriz = MatrizDispersa()


    @app.route('/') 
    def metodo1():
      return "WEB SERVICE PROYECTO 2 "

    @app.route('/reservar',methods=['POST'])#Este metodo ingresa un usuario [Retorna SI se pudo crear el usuario de lo contrario retorna NO]
    def metodo2():
        parametro1 = str(request.form['mes'])
        parametro2 = str(request.form['ano'])
        parametro3 = str(request.form['dia'])

        texto = ""
        if(matriz.verificarExistencia(parametro1,parametro2,parametro3)==0):## vefica si ya existe fecha 
            encabezadomes= matriz.insertar(parametro1)#Envio mi empresa y recibo un nodo empresa
            encabezadofecha = matriz.insertar1(parametro2)#Envio mi depto y recibo el nodo depto
            Nodo = matriz.insertarValor(encabezadomes,parametro3,parametro2,parametro3)
            matriz.unir(encabezadofecha,Nodo)
            texto = "SI"
        else:
            texto = "NO" # ya existe
        return texto

    @app.route('/registro', methods=['POST'])
    def metodo3():

        usuario = str(request.form['usuario'])
        password = str(request.form['password'])
        direccion = str(request.form['direccion'])
        telefono = str(request.form['telefono'])
        edad = str(request.form['edad'])

        listadoble.agregar_inicio(usuario,password,direccion,telefono,edad) # falta agregar datos a la lista doble
        print ("contra verificada y correcta registado")
        return "True"

    @app.route('/ingreso', methods=['POST'])
    def metodo4():

        usuario = str(request.form['usuario'])
        password = str(request.form['password'])

        listadoble.buscar(usuario, password)  # falta agregar datos a la lista doble
        print ("contra verificada y correcta registado")
        return "True"

    @app.route('/habitacioneslista', methods=['POST'])
    def metodo4():

        nivel= str(request.form['nivel'])
        numero = str(request.form['numero'])
        codigo = str(nivel+numero)

        listasimple.agregar_inicio(codigo,nivel,numero)

        print ("habitaciones en lista")
        return "True"


    @app.route('/gastosavl', methods=['POST'])
    def metodo5():

        cuenta= str(request.form['cuenta'])
        monto = str(request.form['monto'])

        avl.insertar(cuenta,monto)

        print ("monto y cuenta ingresado al avl")
        return "True"


    if __name__ == "__main__":
        app.run(debug=True, host='0.0.0.0')

