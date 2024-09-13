from modelo.comprobacion.modeloUsuario import *
from vista.mensajes.mensajes_de_alerta import *
import json

class guardado:
    def comprobacion_inicio(usuario,contraseña,nombre,apellido,cedula):
        try:
            guardado.resultado = comparacion_inicio(usuario,contraseña,nombre,apellido,cedula)
        except:
            print("error no pasa del try")
            guardado.resultado = comparacion_inicio(usuario,contraseña,nombre,apellido,cedula)
            
    def comprobacion_registro(usuario,contraseña,nombre,apellido,cedula):
        try:
            guardado.resultado = comparacion_registro(usuario,contraseña,nombre,apellido,cedula)
        except:
            print("error no pasa del try")
            guardado.resultado = comparacion_registro(usuario,contraseña,nombre,apellido,cedula)
    
#------------------linea privada---------------------------------------------
def comparacion_registro(usuario,contraseña,nombre,apellido,cedula):
    with open("guardados/usuarios.txt","r") as comprobar:
        com=comprobar.readline()
        try:
            comprobador = json.loads(com)
            if usuario in comprobador:
                print("el usuario ya esta registrado")
                errores_en_registro.usuario_ya_registrado()
                comprobar.close()
                return "registro"
            else:
                comprobar.close()
                with open("guardados/usuarios.txt","w") as comprobar:
                    rescribir=comprobador
                    rescribir[usuario]={"usuario":usuario,usuario:contraseña,"nombre":nombre,"apellido":apellido,"cedula":cedula}
                    comprobar.write(str(rescribir))
                    comprobar.close()
        except:
            comprobar.close()
            print("no c encontro informacion")
            
def comparacion_inicio(usuario,contraseña,nombre,apellido,cedula):
    with open("guardados/usuarios.txt","r") as comprobar:
        com=comprobar.readline()
        try:
            comprobador = json.loads(com)
            if usuario in comprobador:
                comprobar.close()
                resultado = comprobador[usuario]
                if contraseña == resultado[usuario]:
                    print(comprobador[usuario])
                    print(resultado[usuario])
                    print("terminado")
                else:
                    print(contraseña)
                    print(resultado[usuario])
                    print("contraseña incorrecta")
            else:
                comprobar.close()
                print("perfecto")
        except:
            comprobar.close()
            print("usuario no encontrado")