from Database.db_config import Database
from werkzeug.security import check_password_hash
db = Database()

con = db.GetConnexion()

cursor = con.cursor()
password_hash = cursor.execute('SELECT password FROM tbl_users WHERE username = %s', ('usuario_prueba'))
print(password_hash)
cursor.close()
db.CloseConexion(connection=con)
clave = input('Ingresa la contraseña: ')
if check_password_hash(pwhash=password_hash, password=clave):
    print('si funciona ')