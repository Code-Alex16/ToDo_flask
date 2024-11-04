from App.Database.db_config import Database_connexion
from werkzeug.security import generate_password_hash, check_password_hash

import re

def validated_users(user_email : str = None, password = None):
    #detectar si ingresa con username o email
    is_email = False

    if re.search('@', user_email):
        is_email = True

    # Seleccionar el tipo de busqueda (si usa username o email)
    query = 'SELECT password FROM tbl_users WHERE user_name = %s'

    if is_email:
        query = 'SELECT password FROM tbl_users WHERE email = %s'
    
    values = (user_email,)

    #Buscar en la base de datos y comparar
    try:
        con = Database_connexion.GetConnexion()
        cursor = con.cursor()
        password_hash = cursor.execute(query,values)

    except Exception as e:
        print(f'Error : {e}')

    finally:
        # cerrar conexiones
        cursor.close()
        Database_connexion.CloseConexion(connection=con)

        # comparar y retornar
        if password_hash and check_password_hash(password_hash,password):
            return True
        else:
            return False

def registrer_user(user_name, email, password):
    # validar datos sean correctos
    is_email = False
    is_username = False
    password_hash = generate_password_hash(method='scrypt', salt_length=16, password=password)

    if re.search('@', email):
        is_email = True

    if (len(user_name) < 12):
        is_username = True

    if (is_email and is_username):
        try:
            con = Database_connexion.GetConnexion()
            cursor = con.cursor()
            sql = 'INSERT INTO tbl_users (user_name, email, password) VALUES (%s,%s,%s)'
            values = (user_name, email, password_hash)
            
            cursor.execute(sql, values)
            con.commit()
            
        except Exception as ex:
            print(f'Error al ingresar el usuario: {ex}')
        
        finally:
            cursor.close()
            Database_connexion.CloseConexion(connection=con)


'''
clave = 'prueba'

clave_hash = generate_password_hash(method='scrypt', salt_length=16, password=clave)
print(clave_hash)

if (check_password_hash(pwhash=clave_hash, password=clave)):
    print(f'si son iguales {clave_hash} : {clave}')
'''