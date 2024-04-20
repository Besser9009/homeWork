def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
    print()

print_params()
print_params(6)
print_params(25, 'Текст')
print_params(0, 'Строчка', False)

print_params(b = 25)
print_params(c = [1, 2, 3,])


values_list = [23.04, False, 'String']
values_dict = {'a': 13, 'b': 'Строка', 'c': 3.14}

print_params(*values_list)
print_params(**values_dict)

values_list2 = [13, True]
print_params(*values_list2, 42)

