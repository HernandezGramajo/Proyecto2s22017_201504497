
package com.servlet;


import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.RequestBody;
import com.squareup.okhttp.Response;

import java.net.MalformedURLException;
import java.net.URL;
import java.util.logging.Level;
import javax.servlet.annotation.WebServlet;





/**
 *
 * @author HERNÁNDEZ
 */
@WebServlet(urlPatterns = {"/conexion_registro"})
public class conexion_registro extends HttpServlet {

    
     public static OkHttpClient webClient = new OkHttpClient();
     
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
     try(PrintWriter out = response.getWriter()){
     
        
             
          String usuario =request.getParameter("txtusuario");
          String contra =request.getParameter("txtcontra");
          String verificarpass = request.getParameter("txtcontracompara");
          
         if (contra.equals(verificarpass)) {
             
   
            
           try{
               
         RequestBody formBody = new FormEncodingBuilder()
               .add("usuario", usuario)
                .add("password",contra)
                
                 .build();
        String r = getString("registro", formBody); 
        System.out.println("---"+ r + "---");
        
               if (r.equals("True")) {
                    response.sendRedirect("Loginn.jsp");
               }
               else{
        response.sendRedirect("Registro.jsp");       
               }
                   
           }
           catch(Exception ex){
               out.println("Error  hola :"+ex.getMessage());
           }
          
           
           
     }else{
         
           response.sendRedirect("Registro.jsp");
         
    }
     }
        
   }

  
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        doGet(request, response);
    }
 
    // enviar datos de jsp a flask
     public static String getString(String metodo, RequestBody formBody) {

        try {
            URL url = new URL("http://0.0.0.0:5000/" + metodo);
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response response = webClient.newCall(request).execute();//Aqui obtiene la respuesta en dado caso si hayas pues un return en python
            String respuesta = response.body().string();//y este seria el string de las respuesta
            return respuesta;
        } catch (MalformedURLException ex) {
            java.util.logging.Logger.getLogger(com.servlet.conexionl_login.class.getName()).log(Level.SEVERE, null, ex);
        } catch (Exception ex) {
            java.util.logging.Logger.getLogger(com.servlet.conexionl_login.class.getName()).log(Level.SEVERE, null, ex);
        }
        return null;
    }
    
    

}
