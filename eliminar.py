#####importo mysqldb
from MySQLdb import*

#####creo objeto conexion#####
conexion = connect(host="localhost", user="root", passwd="",db="python")

#####cro objeto cursor######
cur = conexion.cursor()

####FORMULARIO######
while True:
    try:
        ID = int(input("INGRESA LA IDENTIFICACION: "))
        break
    except:
        print("IDENTIFICACION NO VALIDA")

######Ejecuto######
cur.execute("delete from datos where ID = "+str(ID)+";")

conexion.commit()

#####cierro conexion####
cur.close()