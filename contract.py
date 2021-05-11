from web3 import Web3
from eth_utils import to_int, to_text, to_hex
import json

class Test:
    # конструктор
    def __init__(self, address, contract_address):
        self.infura_url = 'https://ropsten.infura.io/v3/02063760b9b4440aab7c3a022a1f8299'
        self.account_address = address
        self.contract_address = contract_address
        self.private_key = 'c21b1507b5545ea3736520fe8359aa7d0d61a2336fc866de9f63b59cc32de0b3'
        self.w3 = Web3(Web3.HTTPProvider(self.infura_url))
        self.w3.eth.defaultAccount = address
        self.balance = self.w3.eth.getBalance(address)
        with open('rosreestr.abi') as f:
            self.abi = json.load(f)
        self.contract = self.w3.eth.contract(address=self.contract_address, abi=self.abi)

    def getBalance(self):
        return self.w3.fromWei(self.balance, 'ether')

    def sendTransaction(self, transaction):
        signed_tr = self.w3.eth.account.signTransaction(transaction, private_key=self.private_key)
        self.w3.eth.sendRawTransaction(signed_tr.rawTransaction)
        return to_hex(signed_tr.hash)

    def changeOwner(self, newOwner):
        if not self.w3.isAddress(newOwner):
            return "Ошибка ввода данных."
        self.nonce = self.w3.eth.getTransactionCount(self.account_address)
        transaction = self.contract.functions.ChangeOwner(newOwner).buildTransaction({
            'gas': 3000000,
            'gasPrice': self.w3.toWei('1', 'gwei'),
            'from': self.account_address,
            'nonce': self.nonce
        })
        self.sendTransaction(transaction)
        return "Операция прошла успешно."

    def getOwner(self):
        return self.contract.functions.GetOwner().call()

    def addHome(self, adr, area, cost):
        self.nonce = self.w3.eth.getTransactionCount(self.account_address)
        transaction = self.contract.functions.AddHome(adr, to_int(text=area), to_int(text=cost)).buildTransaction({
            'gas': 3000000,
            'gasPrice': self.w3.toWei('1', 'gwei'),
            'from': self.account_address,
            'nonce': self.nonce
        })
        self.sendTransaction(transaction)
        return "Операция прошла успешно."

    def getHome(self, adr):
        return self.contract.functions.GetHome(adr).call()

    def getListHome(self):
        return self.contract.functions.GetListHome().call()

    def addEmployee(self, adr, name, position, phone):
        if not self.w3.isAddress(adr):
            return "Ошибка ввода данных."
        self.nonce = self.w3.eth.getTransactionCount(self.account_address)
        transaction = self.contract.functions.AddEmployee(adr, name, position, phone).buildTransaction({
            'gas': 3000000,
            'gasPrice': self.w3.toWei('1', 'gwei'),
            'from': self.account_address,
            'nonce': self.nonce
        })
        self.sendTransaction(transaction)
        return "Операция прошла успешно."

    def editEmployee(self, adr, name, position, phone):
        if not self.w3.isAddress(adr):
            return "Ошибка ввода данных."
        self.nonce = self.w3.eth.getTransactionCount(self.account_address)
        transaction = self.contract.functions.EditEmployee(adr, name, position, phone).buildTransaction({
            'gas': 3000000,
            'gasPrice': self.w3.toWei('1', 'gwei'),
            'from': self.account_address,
            'nonce': self.nonce
        })
        self.sendTransaction(transaction)
        return "Операция прошла успешно."

    def getEmployee(self, adr):
        if not self.w3.isAddress(adr):
            return "Ошибка ввода данных."
        return self.contract.functions.GetEmployee(adr).call()

    def deleteEmployee(self, adr):
        if not self.w3.isAddress(adr):
            return "Ошибка ввода данных."
        self.nonce = self.w3.eth.getTransactionCount(self.account_address)
        transaction = self.contract.functions.DeleteEmployee(adr).buildTransaction({
            'gas': 3000000,
            'gasPrice': self.w3.toWei('1', 'gwei'),
            'from': self.account_address,
            'nonce': self.nonce
        })
        self.sendTransaction(transaction)
        return "Операция прошла успешно."

    def addRequest(self, type, adr, area, cost, adrNewOwner):
        if not self.w3.isAddress(adrNewOwner):
            return "Ошибка ввода данных."
        self.nonce = self.w3.eth.getTransactionCount(self.account_address)
        transaction = self.contract.functions.AddRequest(to_int(text=type), adr, to_int(text=area), to_int(text=cost), adrNewOwner).buildTransaction({
            'gas': 3000000,
            'gasPrice': self.w3.toWei('1', 'gwei'),
            'from': self.account_address,
            'nonce': self.nonce,
            'value': self.w3.toWei('1', 'gwei')
        })
        self.sendTransaction(transaction)
        return "Операция прошла успешно."

    def getRequest(self):
        return self.contract.functions.GetRequest().call()

    def processRequest(self, id):
        self.nonce = self.w3.eth.getTransactionCount(self.account_address)
        transaction = self.contract.functions.ProcessRequest(to_int(text=id)).buildTransaction({
            'gas': 3000000,
            'gasPrice': self.w3.toWei('1', 'gwei'),
            'from': self.account_address,
            'nonce': self.nonce,
            'value': self.w3.toWei('1', 'gwei')
        })
        self.sendTransaction(transaction)
        return "Операция прошла успешно."

    def editCost(self, price):
        self.nonce = self.w3.eth.getTransactionCount(self.account_address)
        transaction = self.contract.functions.EditCost(to_int(text=price)).buildTransaction({
            'gas': 3000000,
            'gasPrice': self.w3.toWei('1', 'gwei'),
            'from': self.account_address,
            'nonce': self.nonce
        })
        self.sendTransaction(transaction)
        return "Операция прошла успешно."

    def getCost(self):
        return self.contract.functions.GetCost().call()