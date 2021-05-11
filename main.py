from web3 import Web3
import json
import string
from contract import Test

def main():
    while True:
        print('''=============================
'get home' - информация о доме
'get list home' - удалить работника
'add home' - добавить дом
'get employee' - информация о работнике
'add employee' - добавить работника
'edit employee' - редактировать работника
'delete employee' - удалить работника
'get request' - получить запросы
'get owner' - получить адрес владельца
'exit' - выйти из программы 
=============================''')
        cmd = input("Введите команду: ")
        if cmd == "get home":
            getHome()
        elif cmd == "get list home":
            getListHome()
        elif cmd == "add home":
            addHome()
        elif cmd == "get employee":
            getEmployee()
        elif cmd == "add employee":
            addEmployee()
        elif cmd == "edit employee":
            editEmployee()
        elif cmd == "delete employee":
            deleteEmployee()
        elif cmd == "get request":
            getRequest()
        if cmd == "get owner":
            getOwner()
        elif cmd == "exit":
            return
        else:
            print("Такой команды нет!")
    return

def getOwner():
    result = contract.getOwner()
    print(result)

def getRequest():
    result = contract.getRequest()
    print(result)
    print("введите 'x' чтобы завершить:")
    while True:
        n = input("Введите 'id' запросов которые вы хотите пустить на обработку: ")
        if n == "x":
            return
        result = contract.processRequest(n)
        print(result)

def getHome():
    n = input("Введите адрес дома: ")
    result = contract.getHome(n)
    print(result)

def getListHome():
    result = contract.getListHome()
    print(result)

def addHome():
    print("Введите 'return' чтобы вернуться")
    adr = input("Введите адрес дома: ")
    if adr == "return":
        return

    area = input("Введите площадь дома: ")
    if area == "return":
        return

    cost = input("Введите цену дома: ")
    if cost == "return":
        return

    result = contract.addRequest("0", adr, area, cost, "0x5B38Da6a701c568545dCfcB03FcB875f56beddC4")
    print(result)

def getEmployee():
    n = input("Введите счет работника: ")
    result = contract.getEmployee(n)
    print(result)

def addEmployee():
    print("Введите 'return' чтобы вернуться")
    adr = input("Введите счет рабочего: ")
    if adr == "return":
        return
    name = input("Введите имя рабочего: ")
    if name == "return":
        return
    position = input("Введите должность рабочего: ")
    if position == "return":
        return
    phone = input("Введите телефонный номер рабочего: ")
    if phone == "return":
        return
    result = contract.addEmployee(adr, name, position, phone)
    print(result)

def editEmployee():
    print("Введите 'return' чтобы вернуться")
    adr = input("Введите счет рабочего: ")
    if adr == "return":
        return
    name = input("Введите имя рабочего: ")
    if name == "return":
        return
    position = input("Введите должность рабочего: ")
    if position == "return":
        return
    phone = input("Введите телефонный номер рабочего: ")
    if phone == "return":
        return
    result = contract.editEmployee(adr, name, position, phone)
    print(result)

def deleteEmployee():
    print("Введите 'return' чтобы вернуться")
    adr = input("Введите счет рабочего: ")
    if adr == "return":
        return
    result = contract.deleteEmployee(adr)
    print(result)

#address = input("Введите введите свой адрес: ")
#contract = Test(address, '0x03b14e05036966B9c1eD39BDc953740490D440eC')
contract = Test('0xD02B60D56f334d05b3675DaA8988FCb5098a7A6D', '0x03b14e05036966B9c1eD39BDc953740490D440eC')
main()