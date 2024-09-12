from modelo.comprobacion.modeloUsuario import *
import json

class guardado:
    def comprobacion(usuario,contraseña):
        try:
            resultado = comparacion(usuario,contraseña)
        except:
            print("error no pasa del try")
            resultado = comparacion(usuario,contraseña)
    
#------------------linea privada---------------------------------------------
def comparacion(usuario,contraseña):
    with open("guardados/usuarios.txt","r") as comprobar:
        com=comprobar.readline()
        try:
            comprobador = json.loads(com)
            if usuario in comprobador:
                if contraseña in comprobador[usuario]:
                    print(comprobador[usuario])
                    resultado = comprobador[usuario]
                    print(resultado[contraseña])
                    print("terminado")
            else:
                print("perfecto")
        except:
            print("no c imprimio nada")
            print(com)
            print(com["b"])
            