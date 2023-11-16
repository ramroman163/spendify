from queries import doQuery

def showExpense(expense, connectionObj):
    translatedExpenses = (
        "Nombre del gasto",
        "Categoría",
        "Moneda",
        "Monto",
        "Método de pago",
        "Cuotas",
        "Intereses",
        "Fecha del gasto",
    )

    for i, (key, value) in enumerate(expense.items()):
        if key == "date":
            print(
                f"Fecha del gasto: {value['day']}/{value['month']}/{value['year']}")
        elif key == "dues":
            if value["total"] == 0:  # Para pagos indefinidos
                if value["paid"] == 0:
                    print(f"Cuotas: -")
                else:
                    print(f"Cuotas: {value['paid']} pagas")
            elif value["total"] > 1:  # Para pagos de varias cuotas
                print(f"Cuotas: {value['paid']} de {value['total']} pagas")
            else:  # Para pagos de una sola vez
                continue
        elif key == "category":
            print(f"{translatedExpenses[i]}: {getCategoryNameByID(expense['category'], connectionObj)}")
        elif key == "payMethod":
            print(f"{translatedExpenses[i]}: {getPayMethodNameByID(expense['payMethod'], connectionObj)}")
        elif key == "interests":
            if expense["dues"]["total"] == 1:  # No mostrar intereses si no hay cuotas
                continue
            print(f"Intereses: {value}%")
        elif key == "amount":
            print(f"Monto: ${value} {getCurrencyNameByID(expense['currency'], connectionObj)}")
        elif key == "currency":  # No mostrar moneda por separado
            continue
        else:
            print(f"{translatedExpenses[i]}: {value}")


def getCurrencyNameByID(currencyID, connectionObj):
    sql = f"SELECT codigo FROM moneda WHERE id = {currencyID}"
    result = doQuery(sql, 'SELECT', connectionObj, doReturn=True)

    return result[0][0]

def getCategoryNameByID(categoryID, connectionObj):
    sql = f"SELECT nombre FROM categoria WHERE id = {categoryID}"
    result = doQuery(sql, 'SELECT', connectionObj, doReturn=True)

    return result[0][0]

def getPayMethodNameByID(payMethodID, connectionObj):
    sql = f"SELECT nombre FROM metodos WHERE id = {payMethodID}"
    result = doQuery(sql, 'SELECT', connectionObj, doReturn=True)

    return result[0][0]