data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5, 'c': {1, 3, 4, 1, 2}},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = 0

def check_lists(list_, result):
    if isinstance(list_, dict):
        list_dop = list(list_)
        for i in range(len(list_)):
            key = list_dop[i]
            if isinstance(list_[key], dict):
                result = check_lists(list_[key], result)
            elif isinstance(list_[key], list):
                result = check_lists(list_[key], result)
            elif isinstance(list_[key], tuple):
                result = check_lists(list_[key], result)
            elif isinstance(list_[key], set):
                list_[i] = list(list_[i])
                result = check_lists(list_[i], result)
            else:
                result = summer_result_dict(result, list_)
                return result
    else:
        for i in range(len(list_)):
            if isinstance(list_[i], dict):
                result = check_lists(list_[i], result)
            elif isinstance(list_[i], list):
                result = check_lists(list_[i], result)
            elif isinstance(list_[i], tuple):
                result = check_lists(list_[i], result)
            elif isinstance(list_[i], set):
                list_[i] = list(list_[i])
                result = check_lists(list_[i], result)
            else:
                result = summer_result_int_str(result, list_[i])
    return result

def summer_result_int_str(result, value):
    if isinstance(value, str):
        result += len(value)
    elif isinstance(value, int):
        result += value
    return result

def summer_result_dict(result, dict_):
    list_dop = list(dict_)
    for i in range(len(list_dop)):
        key = list_dop[i]
        if isinstance(dict_[key], set):
            list_ = list(dict_[key])
            result = check_lists(list_, result)
        else:
            result += dict_[key]
    for i in dict_:
            result += len(i)
    return result

def calculate_structure_sum(list_, result):
    for i in range(len(list_)):
        if isinstance(list_[i], dict):
            result = check_lists(list_[i], result)
        elif isinstance(list_[i], list) or isinstance(list_[i], tuple):
            result = check_lists(list_[i], result)
        elif isinstance(list_[i], str) or isinstance(list_[i], int):
            result = summer_result_int_str(result, list_[i])
    return result

result = calculate_structure_sum(data_structure, result)
print(result)

