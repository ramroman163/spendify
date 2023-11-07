from add import submenuAdd
from search import submenuSearch
from validate import validateOptionInput
import os

while True:
    os.system('cls')
    print('''
\t ----------------------------------
\t             SPENDIFY 
\t ----------------------------------

1️⃣  AÑADIR 📝
Gastos, categorías, presupuesto y método de pago

2️⃣  BUSCAR 🔍
Encuentra gastos específicos

3️⃣  ANALIZAR 📊
Mirá el seguimiento e informe de tus gastos

4️⃣  RESTABLECER 🧹
Borrá todo el historial de tus gastos

5️⃣  SALIR ❌
No te preocupes ¡tus gastos quedan guardados!


----------------------------------
    ''')  
    try:
        menuOption = input("Ingresá una opción: ")
    except KeyboardInterrupt:
        print('\nvuelva pronto')
        exit()

    if (not(validateOptionInput(menuOption, 5))):
        continue
    
    match menuOption:
        case '1':
            submenuAdd()
        case '2':
            submenuSearch()
        case '3':
            print('tres')
        case '4':
            print('cuatro')
        case '5':
            os.system("cls")
            exit()