<%-- 
    Document   : prueba
    Created on : 28/09/2017, 12:27:09 AM
    Author     : HERNÁNDEZ
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
               <link href ="bootstrap.css" type="text/css" rel="stylesheet">
        <title>JSP Page</title>
    </head>
    <body>
        <br><br><br><br><br>
    <center><h1>REGISTRO</h1></center>
    <br>
        <form action="conexionl_login" method ="POST">
            
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
