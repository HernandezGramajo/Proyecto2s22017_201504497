<%-- 
    Document   : Loginn
    Created on : 18/09/2017, 10:36:38 PM
    Author     : HERNÁNDEZ
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <title>LOGIN</title>
        <link href ="bootstrap.css" type="text/css" rel="stylesheet">       
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
       
    </head>
<body><br><br><br><br><br>
    <center><h1>LOGIN</h1></center>
    <br>
        <form action="conexionl_login" method ="POST">
            
            <table align ="center">
                <tr>
                    <th align="right">USUARIO:</th>
                    <td><input type="text" name ="txtusuario" placeholder = "Username"></td>
                </tr>
                <tr>
                    <th align="right">CONTRASEÑA:</th>
                    <td><input type="text" name ="txtcontra" placeholder = "Password"></td>
                </tr>
                <tr>
                    <td colspan="2" align ="right"><input type ="submit" value = "Log In" class="btn btn-primary"></td>
                    <td colspan="1" align ="left" ><p>    </p><a href="Registro.jsp">Registrarse</a></td>
                </tr>

            </table>
        </form>
    </body>
</html>
