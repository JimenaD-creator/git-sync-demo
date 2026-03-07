# Imprimir Hola Mundo desde el sistema operativo y la arquitectura actuales 
# python app.py 
import platform 
if __name__ == '__main__' : 
    # Obtener el nombre del sistema operativo
    os_name = platform.system() 
    # Obtener la arquitectura del sistema
    arquitectura = platform.architecture() 
    print ( f"¡Hola Mundo! desde el sistema operativo {os_name} en la arquitectura {arquitectura[ 0 ]}  {arquitectura[ 1 ]} arquitectura" ) 
else : 
    pass
