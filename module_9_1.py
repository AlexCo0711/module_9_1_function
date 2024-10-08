# Домашнее задание по теме "Введение в функциональное программирование"
# объявление функции apply_all_func, которая вызывает функцию functions к списку int_list
def apply_all_func(int_list, *functions):
    # объявление словаря result
    results = {}
    # цикл перебора функций обращения
    for f in functions:
        # формирование словаря result {функция : результат работы функции со списком}
        results[f.__name__] = f(int_list)
    # возврат работы функции apply_all_func - словарь result
    return results

# объявление функции минимального элемента из списка int_list
def min_arg(int_list):
    # возврпат работы функции
    return min(int_list)
# объявление функции максимального элемента из списка arg (arg = int_list)
def max_arg(arg):
    # возврпат работы функции
    return max(arg)
# объявление функции подсчета элементов списка arg
def len_arg(arg):
    # возврпат работы функции
    return len(arg)
# объявление функции суммы элементов списка arg
def sum_arg(arg):
    # возврпат работы функции
    return sum(arg)
# объявление функции сортировки списка arg
def sorted_arg(arg):
    # возврпат работы функции
    return sorted(arg)

# исходные данные и вывод на консоль
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))