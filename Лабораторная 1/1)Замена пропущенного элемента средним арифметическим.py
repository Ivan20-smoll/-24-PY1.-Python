numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
numbers = [2, -93, -2, 8, None, -0.44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# Находим индекс значения None
index = numbers.index(None)

# Создаем новый список, исключая None, для расчета среднего арифметического
numbers_without_none = [num for num in numbers if num is not None]

# Вычисляем среднее арифметическое
average = sum(numbers_without_none) / len(numbers_without_none)

# Заменяем значение None на вычисленное среднее
numbers[index] = average

print("Измененный список:", numbers)






