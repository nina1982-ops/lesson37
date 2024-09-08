# def personal_sum(numbers):
#     result = 0
#     incorrect_data = 0
#     for num in numbers:
#         try:
#             result += numbers
#         except TypeError:
#             incorrect_data += 1
#     return result, incorrect_data
#
# def calculate_average(numbers):
#
#         try:
#             sum_numbers, incorrect_data = personal_sum(numbers)
#             if len(numbers) > 0:
#                 return sum_numbers / len(numbers)
#             else:
#                 return None
#
# try:
#
# except TypeError:
#     print('В numbers записан некорректный тип данных'))
#
#
#     # Пример выполнения программы:
#     print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
#     print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
#     print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
#     print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать


def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for number in numbers:
        try:
            result += number
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {number}')

    return result, incorrect_data
def calculate_average(numbers):
    try:
        sum_numbers, incorrect_data = personal_sum(numbers)
        return sum_numbers / incorrect_data if incorrect_data > 0 else 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None

# Пример выполнения программы:
print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
