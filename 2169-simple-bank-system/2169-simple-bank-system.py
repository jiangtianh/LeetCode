class Bank:

    def __init__(self, balance: List[int]):
        self.d = {}
        for i, b in enumerate(balance):
            self.d[i+1] = b

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 in self.d and account2 in self.d and self.d[account1] >= money:
            self.d[account1] -= money
            self.d[account2] += money
            return True
        return False
        

    def deposit(self, account: int, money: int) -> bool:
        if account in self.d:
            self.d[account] += money
            return True
        return False
        

    def withdraw(self, account: int, money: int) -> bool:
        if account in self.d and self.d[account] >= money:
            self.d[account] -= money
            return True
        return False
    


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)