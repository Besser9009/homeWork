immutable_var = 3, False, "string", 3.23
print(immutable_var)

# immutable_var[1] = True # данное действие выполнить невозможно, так как кортеж неизменяем
mutable_list = [32, "sea", 1, "Petrov"]
mutable_list[3] = "Ivanov"
print(mutable_list)