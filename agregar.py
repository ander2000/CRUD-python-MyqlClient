########IMPORTO MysqlClient
from MySQLdb import*

########objeto conexion#######
conexion = connect(host="localhost", user="root", passwd="",db="python")

########objeto cursor###########
cur = conexion.cursor()

########FORMULARIO########

while True:
    nombre = input("INGRESA EL NOMBRE ")
    if nombre.isalpha() == True:
        break
    else:
        print("NOMBRE NO VALIDO")

while True:
    apellidos = input("INGRESA APELLIDO ")
    if apellidos.isalpha() == True:
        break
    else:
        print("APELLDO NO VALIDO")


#########EJECUTO LA CONSULTA#######
cur.execute("insert into datos values (null, '"+ nombre +"', '"+ apellidos +"')")

conexion.commit()

#########cierro conexion#########
cur.close()