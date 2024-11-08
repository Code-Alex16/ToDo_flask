from Databases.config_db import Database

from werkzeug.security import check_password_hash



db = Database()
conexion = db.GetConnexion()

cursor  = conexion.cursor()

cursor.execute('SELECT * FROM tbl_users')

data = cursor.fetchone()

password_hash = data[3]

clave = input('ingrese la clave> ')

if check_password_hash(pwhash=password_hash, password=clave):
    print('si funciona ')


print(clave)
print(password_hash)
