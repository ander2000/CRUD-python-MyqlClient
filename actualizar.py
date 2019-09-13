####IMPORTO MYSQLCLIENT######
from MySQLdb import*

####CREO OBJETO CONEXION#####
conexion = connect(host="localhost", user="root", passwd="",db="python")

####CREO OBJETO CURSOR######
cur = conexion.cursor()

#####formulario######
while True:
    nombre = input("INGRESA EL NUEVO NOMBRE ")
    if nombre.isalpha() == True:
        break
    else:
        print("NOMBRE NO VALIDO")

while True:
    apellidos = input("INGRESA LO NUEVO APELLIDO ")
    if apellidos.isalpha() == True:
        break
    else:
        print("APELLDO NO VALIDO")

while True:
    try:
        ID = int(input("INGRESE LA IDENTIFICACION "))
        break
    except:
        print("IDENTIFICACION NO VALIDA ")



####EJECUTO#######
cur.execute("update datos set nombre = '"+ nombre +"', apellidos = '"+ apellidos +"' where ID = "+ str(ID) +" ")
conexion.commit()

#####CIERRO CONEXION#####   
conexion.close()