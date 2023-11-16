import os
from utilities import validateInputs
from queries import doQuery

budget = {"currency": 0, "amount": 0}

def addBudget(connectionObj):
    os.system("cls")

    currencyList = getCurrencies(connectionObj)

    currencyNameList = list(map(getCurrencyName, currencyList))
   
    currencyNameIndex = validateInputs.inputOptionModel(
        "tipo de moneda", currencyNameList, defaultValue=0, convertValue=False
    )
    
    currencyNameIndex = 1 if currencyNameIndex == 0 else currencyNameIndex

    amount = validateInputs.inputModel(
        "monto del presupuesto", isNumber=True, isRange=[1, 100000000]
    )

    chosenCurrencyName = currencyNameList[currencyNameIndex-1]
    
    chosenCurrencyID = getCurrencyID(chosenCurrencyName, currencyList) 
      
    os.system("cls")
    print(
        """
>> AÑADIR > PRESUPUESTO FINAL
← VOLVER (V)

//////////////////////////////////////"""
    )

    print(f"Moneda: {chosenCurrencyName}")
    print(f"Monto: {int(amount)}")
    
    budget['amount'] = amount
    budget['currency'] = chosenCurrencyID

    if checkUserExistence(connectionObj) <= 0:
        saveUserBudget(connectionObj, budget)
    else:
        updateUserBudget(connectionObj, budget)

    input(
        """
//////////////////////////////////////
\n\nENTER para volver al menú """
    )
    os.system("cls")

def checkUserExistence(connectionObj):
    sql = "SELECT nombre FROM usuarios"
    result = doQuery(sql, 'SELECT', connectionObj, doReturn=True)

    return len(result)

def saveUserBudget(connectionObj, budget):
    print(budget)
    sql = "INSERT INTO usuarios (nombre, moneda, presupuesto, presupuesto_actual) VALUES (%s, %s, %s, %s)"
    values = ("test", budget['currency'], budget['amount'], budget['amount'])
    doQuery(sql, 'INSERT', connectionObj, values=values)

def updateUserBudget(connectionObj, budget):
    print(budget)
    sql = f"UPDATE usuarios SET nombre = '{'test'}', moneda = {budget['currency']}, presupuesto = {budget['amount']}, presupuesto_actual = {budget['amount']} WHERE id = 1"
    doQuery(sql, 'UPDATE', connectionObj)

def getCurrencies(connectionObj):
    sql = "SELECT id, codigo, nombre FROM moneda"
    result = doQuery(sql, 'SELECT', connectionObj, doReturn=True)

    currenciesData = []

    for currency in result:
        currenciesData.append({ "id": currency[0], "codigo": currency[1], "nombre": currency[2]})

    return currenciesData


def getCurrencyID(currencyName, currencyList):
    for currency in currencyList:
        if(currencyName == currency["nombre"]):
            return currency["id"]
    
    return 0

def getCurrencyName(currency):
    return currency["nombre"]