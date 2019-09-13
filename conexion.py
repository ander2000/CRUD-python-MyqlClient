#######IMPORTO MysqlLbd########
from MySQLdb import*

#######OBJETO CONEXION#####
conexion = connect(host="localhost", user="root", passwd="",db="python")

#######OBJETO CURSOR PARA LAS CONSULTAS Y SE ESPECIFICA LA CONEXION#######
cur = conexion.cursor()

#######AGREGO A LA BASE DE DATOS#######
cur.execute("select * from datos;")

#######MUESTRO BASE DE DATOS###########
for datos in cur.fetchall() :
    print(datos)

#######CIERRO LA CONEXION A LA BASE DE DATOS######## 
cur.close()