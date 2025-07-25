import datetime
from conexionBD import *
import hashlib

def hash_passowrd(contrasena):
    return hashlib.sha256(contrasena.encode()).hexdigest()

def registrar(nombre,apellidos,email,contrasena):
    try:
        fecha=datetime.datetime.now()
        contrasena=hashlib.sha256(contrasena.encode()).hexdigest()
        sql="insert into usuarios (nombre, apellidos, email, password, fecha) values (%s, %s, %s, %s, %s)"
        val=(nombre,apellidos,email,contrasena,fecha)
        cursor.execute(sql,val)
        conexion.commit() 
        return True
    except:
        return False
    
def iniciar_sesion(email,contrasena):
    try:
        contrasena=hashlib.sha256(contrasena.encode()).hexdigest()
        sql="select * from usuarios where email=%s and password=%s"
        val=(email,contrasena)
        cursor.execute(sql,val)
        registros=cursor.fetchone()
        if registros:
         return registros
        else:
            return None
    except:
        return None