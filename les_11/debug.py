from custom_iterator import User


def foo():
    a = 'foo'

    def baz():
        b = 'baz'

        def bar():
            c = 'bar'
            1/0
            return c

        return bar()
    return baz()


foo()

alex = User('Alex', 'Hjks8320djsdf', 30, 'Belarus')
