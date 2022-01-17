class Customer:
    last_id = 0

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        Customer.last_id += 1
        self.id = Customer.last_id

    def __repr__(self):
        return 'Customer[{},{},{},{}]'.format(self.id, self.first_name, self.last_name, self.email)


class Account:
    last_id = 0


    def __init__(self, customer):
        Account.last_id += 1
        self.id = Account.last_id
        self.customer = customer
        self._balance = 0


    def charge(self, amount):
        if self._balance >= amount:
            self._balance -= amount
        else:
            print('Insuffecient Balance')


    def deposit(self, amount):
        self._balance += amount


    def get_balance(self):
        return self._balance


    def __repr__(self):
        return '{}[{},{},{}]'.format(self.__class__.__name__, self.id, self.customer.last_name, self._balance)


class SavingsAccount(Account):
    interest_rate = 0.02

    def calc_interest(self):
        self._balance += self.interest_rate * self._balance


class CheckingAccount(Account):
    pass


class Bank:
    def __init__(self):
        self.cust_list = []
        self.acc_list = []


    def new_customer(self, first_name, last_name, email):
        c = Customer(first_name, last_name, email)
        self.cust_list.append(c)
        return c


    def new_account(self, customer, is_savings=True):
        a = SavingsAccount(customer) if is_savings else CheckingAccount(customer)
        self.acc_list.append(a)
        return a


    def get_account(self, account_id):
        return [account for account in self.acc_list if account.id == account_id]


    def is_valid_transfer(self, from_account, to_account, amount):
        is_valid_transfer = False
        if from_account and to_account:
            if from_account[0].get_balance() >= amount:
                is_valid_transfer = True
        return is_valid_transfer


    def transfer(self, from_account_id, to_account_id, amount):
        from_account, to_account = self.get_account(from_account_id), self.get_account(to_account_id)
        if self.is_valid_transfer(from_account, to_account, amount):
            to_account[0].deposit(amount)
            from_account[0].charge(amount)
        else:
            print('Invalid Transfer request')


    def __repr__(self):
        return 'Bank\n{}\n{}'.format(self.cust_list, self.acc_list)

b = Bank()

c1 = b.new_customer('John', 'Brown', 'john@brown.com')
c2 = b.new_customer('Anna', 'Smith', 'anne@smith.com')

a1 = b.new_account(c1, is_savings=True)
a2 = b.new_account(c1, is_savings=False)

print(b)


a1.deposit(10)
b.transfer(a1.id,a2.id,5)