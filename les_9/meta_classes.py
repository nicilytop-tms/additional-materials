def choose_class(name):
    if name == 'foo':
        class Foo:
            pass

        return Foo
    else:
        class Bar:
            pass

        return Bar


MyClass = choose_class('foo')

#######################################################################################################################

MyShinyClass = type('MyShinyClass', (), {})
print(MyShinyClass)

msc = MyShinyClass()
print(msc)

#######################################################################################################################

BankAccount = type('BankAccount', (), {'BONUS': 30})
peters_account = BankAccount()
harisons_account = BankAccount()

harisons_account.BONUS = 20
print(harisons_account.BONUS)
print(peters_account.BONUS)
