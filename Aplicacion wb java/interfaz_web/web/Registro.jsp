<%-- 
    Document   : Registro
    Created on : 19/09/2017, 11:08:43 AM
    Author     : HERNÁNDEZ
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <title>Registro</title>
        <link href ="bootstrap.css" type="text/css" rel="stylesheet">       
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
       
    </head>
<body><br><br><br><br><br>
    <center><h1>REGISTRO</h1></center>
    <br>
        <form action="conexion_registro" method ="POST">
            
            <table align ="center">
                <tr>
                    <th align="right">Nombre de Usuario:</th>
                    <td><input type="text" name ="txtusuario" placeholder = "Username"></td>
                </tr>
                <tr>
                    <th align="right">Contraseña:</th>
                    <td><input type="text" name ="txtcontra" placeholder = "contraseña"></td>
                </tr>
                                <tr>
                    <th align="right">Verificar Cotraseña:</th>
                    <td><input type="text" name ="txtcontracompara" placeholder = "comparar contrseña"></td>
                </tr>
                <tr>
                    <td colspan="2" align ="right"><input type ="submit" value = "Registrar" class="btn btn-primary"></td>
                    <td colspan="1" align ="left" ><p>    </p><a href="Loginn.jsp">atras</a></td>
                </tr>

            </table>
        </form>
    </body>
</html>
