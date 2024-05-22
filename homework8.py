def print_params(a=1, b='Строка', c=True):
    print(a, b, c)
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [1, "Hello", (1, 2, 3)]
values_dict = {"a": 10, "b": 20, "c": 30}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [13, (6, 5, 4)]
print_params(*values_list_2, 42)
