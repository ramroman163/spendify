import os
from validate import inputModel

def submenuSearchByString(option):
    message = ''
    match option:
        case '1':
            message = 'BÚSQUEDA POR NOMBRE'
        case '2':
            message =  'BÚSQUEDA POR CATEGORÍA'
        case '3':
            message = 'BÚSQUEDA POR MÉTODO DE PAGO'

    while True:
        os.system("cls")
        print(f'''
{message} 
----------------------------------
                ''')
        name = input('Cadena a buscar: ')
        print(name)
        enter = input("\nPresione ENTER para volver al menú")
        break
    return



        
        
