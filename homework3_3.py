def test(*params, t = False, n = 13, s = 'string', **value):
    print(t, n, s)
    print(*params)
    sum = 0
    for i in range(len(params)):
        sum += params[i]
    print(sum)
    print(value)
    for key, value in value.items():
        print(key, ":", value)
test(12, 24, 34, 0, -12, 99, t = True, s = 'Строка', name = "Miolit", age = 21, interesting = "Python")

print()

def recurs(n):
    if n == 1:
        return 1
    else:
        return n * recurs(n-1)
print(recurs(5))