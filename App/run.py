from flask import Flask, render_template, request, redirect, url_for
from functions.funtions_users import *
app = Flask(__name__)

@app.route('/')
def pagina_principal():
    return render_template('pagina_principal.html')

@app.route('/login', methods = ['POST','GET'])
def login_user():
    if request.method == 'POST':
        user_email = request.form.get('email')
        password = request.form.get('password')

        if not(validated_users(user_email, password)):
            return redirect(url_for('login_user', msg='Usuario no existente'))
        
        return redirect(url_for('pagina_usuario'))
        
    return render_template('login.html')

@app.route('/resgistro', methods = ['POST'])
def user_registrer():
    return render_template('registro.html')

@app.errorhandler(404)
def page_not_found():
    return render_template('error_404.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)