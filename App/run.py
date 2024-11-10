import os
from dotenv import load_dotenv
from functions.validations_data import validated_users, registrer_user
from flask import Flask, render_template, request, redirect, url_for

load_dotenv()   #cargar variables de entorno

#configurar app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

## USUARIOS ##
@app.route('/')
def pagina_principal():
    return render_template('pagina_principal.html')

@app.route('/login', methods = ['POST','GET'])
def login_user():
    if request.method == 'POST':
        user_email = request.form.get('email')
        password = request.form.get('password')

        if not(validated_users(user_email, password)):
            return redirect(url_for('login_user', msg='Contraseña no valida'))
        
        return redirect(url_for('pagina_principal'))
        
    return render_template('login.html')

@app.route('/resgistro', methods = ['POST','GET'])
def user_registrer():

    if request.method == 'POST':
        user_name = request.form.get('user_name')
        email = request.form.get('email')
        password = request.form.get('password')

        if not(registrer_user(user_name,email,password)):
            return redirect(url_for('user_registrer', msg='datos invalidos'))
        
        return redirect(url_for('login_user', msg = 'Ahora puede Iniciar sesion'))

    return render_template('registro.html')

## Task ##

## ERRORES ##
@app.errorhandler(404)
def page_not_found():
    return render_template('error_404.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)