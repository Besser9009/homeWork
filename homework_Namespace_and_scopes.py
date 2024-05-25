def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()

test_function()

# inner_function()  Вызов не сработает так как она находится в локальном пространстве имён функции test_function()

