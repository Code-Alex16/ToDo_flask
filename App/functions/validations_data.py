import sys
import os
import re

# Agregar la ruta absoluta de la carpeta "App" al sistema de rutas
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Databases')))

from werkzeug.security import generate_password_hash, check_password_hash
from config_db import Database


def validated_users(user_email = None, password_user = None):
    DB = Database()
    password_hash : str = ''
    
    query = 'SELECT password FROM tbl_users WHERE user_name = %s'

    if re.search('@', user_email):
        query = 'SELECT password FROM tbl_users WHERE email = %s'
  
    values = (user_email, )
    
    try:
        con = DB.GetConnexion()
        cursor = con.cursor()
        cursor.execute(query,values)
        result = cursor.fetchone()

        if result: 
            password_hash = result[0]

            if check_password_hash(pwhash=password_hash,password = password_user):
                return True
        
        return False

    except Exception as e:
        print(f'Error : {e}')

    finally:
        cursor.close()
        DB.CloseConexion(connection=con)


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
            con = Database.GetConnexion()
            cursor = con.cursor()
            sql = 'INSERT INTO tbl_users (user_name, email, password) VALUES (%s,%s,%s)'
            values = (user_name, email, password_hash)
            
            cursor.execute(sql, values)
            con.commit()
            
        except Exception as ex:
            print(f'Error al ingresar el usuario: {ex}')
        
        finally:
            cursor.close()
            Database.CloseConexion(connection=con)

'''
clave = 'prueba'

clave_hash = generate_password_hash(method='scrypt', salt_length=16, password=clave)
print(clave_hash)

if (check_password_hash(pwhash=clave_hash, password=clave)):
    print(f'si son iguales {clave_hash} : {clave}')
'''